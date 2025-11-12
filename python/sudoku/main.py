import pygame
import sys
import time
from sudoku import Sudoku 


pygame.font.init()


WIDTH = 540  # 9 celdas * 60 pixeles
HEIGHT = 640 # 540 para la parrilla + 100 para la UI
CELL_SIZE = WIDTH // 9

# Colores (R, G, B)
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)
COLOR_GRIS_CLARO = (230, 230, 230)
COLOR_LINEA = (180, 180, 180)
COLOR_SELECCION = (0, 100, 255)
COLOR_NUM_ORIGINAL = (40, 40, 40)
COLOR_NUM_USUARIO = (60, 60, 180)
COLOR_NUM_ERROR = (200, 0, 0)
COLOR_NOTAS = (120, 120, 120)
COLOR_FONDO_UI = (245, 245, 245)

# Fuentes
FONT_NUMEROS = pygame.font.SysFont("Arial", 40)
FONT_NOTAS = pygame.font.SysFont("Arial", 16)
FONT_UI = pygame.font.SysFont("Arial", 22)
FONT_FIN = pygame.font.SysFont("Arial", 50)
FONT_FIN_SUB = pygame.font.SysFont("Arial", 25)

class Board:
    """
    Gestiona la lógica y el dibujo de un único tablero de Sudoku.
    """
    def __init__(self, difficulty_float):
        # 1. Generar el tablero usando la biblioteca 'sudoku'
        # El generador de la biblioteca asegura una solución única.
        # La dificultad va de 0.0 (fácil) a 1.0 (difícil)
        puzzle = Sudoku(3, 3).difficulty(difficulty_float)
        
        # 2. Convertir el formato del tablero (None -> 0)
        self.original_board = self.convert_board(puzzle.board)
        self.solution_board = self.convert_board(puzzle.solve().board)
        self.user_board = [row[:] for row in self.original_board] # Copia profunda
        
        # 3. Estado de la interfaz
        self.selected_cell = None  # (fila, col)
        self.is_notes_mode = False
        self.notes = {}  # {(fila, col): set(1, 2, ...)}

    def convert_board(self, board_from_lib):
        """Convierte un tablero de la biblioteca (con 'None') a nuestro formato (con '0')."""
        new_board = []
        for row in board_from_lib:
            new_row = []
            for item in row:
                new_row.append(item if item is not None else 0)
            new_board.append(new_row)
        return new_board

    def draw(self, screen):
        """Dibuja la parrilla, los números y la selección."""
        screen.fill(COLOR_BLANCO)
        
        # Dibujar líneas de la parrilla
        for i in range(10):
            grosor = 3 if i % 3 == 0 else 1 # Líneas gruesas para cajas 3x3
            pygame.draw.line(screen, COLOR_NEGRO, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), grosor)
            pygame.draw.line(screen, COLOR_NEGRO, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), grosor)
            
        # Dibujar números y notas
        for r in range(9):
            for c in range(9):
                num = self.user_board[r][c]
                
                if num == 0:
                    # Dibujar notas si existen
                    if (r, c) in self.notes:
                        self.draw_cell_notes(screen, r, c)
                else:
                    # Dibujar número
                    color = COLOR_NUM_ORIGINAL
                    if self.original_board[r][c] == 0: # Es un número del usuario
                        if num == self.solution_board[r][c]:
                            color = COLOR_NUM_USUARIO
                        else:
                            color = COLOR_NUM_ERROR # Error visible
                            
                    self.draw_cell_number(screen, str(num), (r, c), color)

        # Resaltar celda seleccionada
        if self.selected_cell:
            r, c = self.selected_cell
            pygame.draw.rect(screen, COLOR_SELECCION, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    def draw_cell_number(self, screen, text, pos, color):
        """Dibuja un número grande centrado en su celda."""
        r, c = pos
        text_surface = FONT_NUMEROS.render(text, True, color)
        text_rect = text_surface.get_rect(center=(c * CELL_SIZE + CELL_SIZE // 2, r * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(text_surface, text_rect)

    def draw_cell_notes(self, screen, r, c):
        """Dibuja los números de notas (modo lápiz) en una celda."""
        cell_notes = self.notes.get((r, c), set())
        for num in cell_notes:
            text_surface = FONT_NOTAS.render(str(num), True, COLOR_NOTAS)
            # Posiciona cada nota en una mini-parrilla 3x3 dentro de la celda
            row_in_cell = (num - 1) // 3
            col_in_cell = (num - 1) % 3
            pos_x = c * CELL_SIZE + (col_in_cell * (CELL_SIZE // 3)) + (CELL_SIZE // 6)
            pos_y = r * CELL_SIZE + (row_in_cell * (CELL_SIZE // 3)) + (CELL_SIZE // 6)
            text_rect = text_surface.get_rect(center=(pos_x, pos_y))
            screen.blit(text_surface, text_rect)

    def handle_click(self, pos):
        """Actualiza la celda seleccionada basado en la posición del ratón."""
        if pos[1] < WIDTH: # Asegurarse de que el clic es dentro de la parrilla
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            self.selected_cell = (row, col)

    def place_number(self, num):
        """Coloca un número o una nota en la celda seleccionada."""
        if not self.selected_cell:
            return False, False # (movimiento_hecho, es_error)

        r, c = self.selected_cell
        
        # No se puede cambiar un número original
        if self.original_board[r][c] != 0:
            return False, False

        # Modo Notas (Lápiz)
        if self.is_notes_mode:
            if (r, c) not in self.notes:
                self.notes[(r, c)] = set()
            
            if num in self.notes[(r, c)]:
                self.notes[(r, c)].remove(num)
            else:
                self.notes[(r, c)].add(num)
            
            # Limpiar el número principal si estamos poniendo notas
            self.user_board[r][c] = 0
            return False, False # No fue un movimiento final
        
        # Modo Normal (Pluma)
        else:
            # Limpiar notas si ponemos un número
            self.notes.pop((r, c), None)
            
            # Colocar el número
            self.user_board[r][c] = num
            
            # Validar movimiento
            es_error = (num != self.solution_board[r][c])
            return True, es_error

    def clear_number(self):
        """Borra el número o las notas de la celda seleccionada."""
        if self.selected_cell:
            r, c = self.selected_cell
            if self.original_board[r][c] == 0:
                self.user_board[r][c] = 0
                self.notes.pop((r, c), None)

    def is_complete(self):
        """Verifica si el tablero está completo y es correcto."""
        return self.user_board == self.solution_board

class Game:
    """
    Gestiona el estado general del juego, la progresión de niveles,
    las vidas, el tiempo y el bucle principal.
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku Interactivo")
        self.clock = pygame.time.Clock()
        
        self.level_names = ["Muy Fácil", "Fácil", "Medio", "Difícil", "Experto"]
        # Mapeo de dificultad para la biblioteca 'sudoku'
        self.difficulty_map = [0.3, 0.4, 0.5, 0.6, 0.75]
        
        self.wants_to_restart = False
        self.start_new_game()

    def start_new_game(self):
        """Inicializa o reinicia todas las variables del juego."""
        self.lives = 3
        self.current_level_index = 0
        self.current_board_in_level = 0
        
        self.start_time = time.time()
        self.total_time_str = "00:00"
        
        self.running = True
        self.game_over = False
        self.game_won = False
        
        self.bonus_life_pending = False
        self.lives_lost_this_board = 0
        
        self.board = self.create_new_board()
        
    def create_new_board(self):
        """Crea un nuevo tablero, aplicando el bonus de vida si corresponde."""
        if self.bonus_life_pending:
            self.lives += 1
            self.bonus_life_pending = False
            
        self.lives_lost_this_board = 0
        difficulty_float = self.difficulty_map[self.current_level_index]
        return Board(difficulty_float)

    def run(self):
        """Bucle principal del juego."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30) # 30 FPS es suficiente

        # Cuando self.running es False, mostrar la pantalla final
        self.show_end_screen()

    def handle_events(self):
        """Gestiona todos los inputs del usuario (ratón, teclado)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.wants_to_restart = False # Salir completamente
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.handle_click(pygame.mouse.get_pos())
                
            if event.type == pygame.KEYDOWN:
                if self.board.selected_cell:
                    num = -1
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1: num = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2: num = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3: num = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4: num = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5: num = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6: num = 6
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7: num = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8: num = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9: num = 9
                    
                    if num != -1:
                        movimiento_hecho, es_error = self.board.place_number(num)
                        
                        if movimiento_hecho and es_error:
                            self.lose_life()
                            
                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        self.board.clear_number()
                        
                # Alternar modo notas
                if event.key == pygame.K_SPACE:
                    self.board.is_notes_mode = not self.board.is_notes_mode

    def update(self):
        """Actualiza la lógica del juego (cronómetro, victoria/derrota)."""
        # Actualizar cronómetro
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        self.total_time_str = f"{minutes:02}:{seconds:02}"
        
        # Comprobar si el tablero está completo
        if self.board.is_complete():
            self.advance_to_next_board()

    def draw(self):
        """Dibuja todos los elementos en la pantalla."""
        self.board.draw(self.screen)
        self.draw_ui()
        pygame.display.flip()

    def draw_ui(self):
        """Dibuja la interfaz de usuario inferior (vidas, nivel, tiempo)."""
        # Fondo
        pygame.draw.rect(self.screen, COLOR_FONDO_UI, (0, WIDTH, WIDTH, HEIGHT - WIDTH))
        pygame.draw.line(self.screen, COLOR_LINEA, (0, WIDTH), (WIDTH, WIDTH), 2)
        
        # Vidas
        vidas_txt = f"Vidas: {self.lives}"
        text_surface = FONT_UI.render(vidas_txt, True, COLOR_NEGRO)
        self.screen.blit(text_surface, (15, WIDTH + 15))
        
        # Nivel y Progreso
        nivel_txt = f"{self.level_names[self.current_level_index]} ({self.current_board_in_level + 1}/3)"
        text_surface = FONT_UI.render(nivel_txt, True, COLOR_NEGRO)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, WIDTH + 30))
        self.screen.blit(text_surface, text_rect)
        
        # Cronómetro
        tiempo_txt = f"Tiempo: {self.total_time_str}"
        text_surface = FONT_UI.render(tiempo_txt, True, COLOR_NEGRO)
        text_rect = text_surface.get_rect(topright=(WIDTH - 15, WIDTH + 15))
        self.screen.blit(text_surface, text_rect)
        
        # Modo Notas
        modo_txt = "Modo: NOTAS (Espacio)" if self.board.is_notes_mode else "Modo: NORMAL (Espacio)"
        text_surface = FONT_UI.render(modo_txt, True, COLOR_GRIS_CLARO if self.board.is_notes_mode else COLOR_NEGRO)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, WIDTH + 70))
        self.screen.blit(text_surface, text_rect)

    def lose_life(self):
        """Resta una vida y comprueba si es Game Over."""
        self.lives -= 1
        self.lives_lost_this_board += 1
        if self.lives <= 0:
            self.game_over = True
            self.running = False # Termina el bucle principal

    def advance_to_next_board(self):
        """Avanza al siguiente tablero o nivel, o gana el juego."""
        
        # Comprobar si se ganó vida extra
        if self.lives_lost_this_board == 0:
            self.bonus_life_pending = True
            
        self.current_board_in_level += 1
        
        if self.current_board_in_level == 3: # Completó 3 tableros
            self.current_board_in_level = 0
            self.current_level_index += 1
            
            if self.current_level_index == len(self.level_names): # Completó 5 niveles
                self.game_won = True
                self.running = False
                return

        # Crear el siguiente tablero
        self.board = self.create_new_board()
        pygame.time.wait(500) # Pequeña pausa para que el jugador note el cambio

    def show_end_screen(self):
        """Muestra la pantalla de Victoria o Derrota."""
        
        # Superposición oscura
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180)) # Negro con transparencia
        self.screen.blit(overlay, (0, 0))
        
        # Mensaje de Fin
        if self.game_won:
            msg = "¡VICTORIA!"
            color = (0, 200, 0)
        elif self.game_over:
            msg = "GAME OVER"
            color = COLOR_NUM_ERROR
        
        # Dibujar textos
        msg_surf = FONT_FIN.render(msg, True, color)
        msg_rect = msg_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.screen.blit(msg_surf, msg_rect)
        
        time_surf = FONT_FIN_SUB.render(f"Tiempo Total: {self.total_time_str}", True, COLOR_BLANCO)
        time_rect = time_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        self.screen.blit(time_surf, time_rect)
        
        restart_surf = FONT_UI.render("Presiona [R] para reiniciar o [Q] para salir", True, COLOR_BLANCO)
        restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
        self.screen.blit(restart_surf, restart_rect)
        
        pygame.display.flip()
        
        # Bucle de espera para reiniciar o salir
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.wants_to_restart = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        waiting = False
                        self.wants_to_restart = False
                    if event.key == pygame.K_r:
                        waiting = False
                        self.wants_to_restart = True

# --- Bucle de Ejecución Principal ---

def main():
    """Permite reiniciar el juego."""
    pygame.init()
    while True:
        game = Game()
        game.run() # El juego se ejecuta aquí
        
        # Al salir de game.run(), comprobamos si el usuario quiere reiniciar
        if not game.wants_to_restart:
            break # Sale del bucle 'while True'
            
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()