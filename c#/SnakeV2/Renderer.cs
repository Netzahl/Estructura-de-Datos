using System.Numerics;
using Raylib_cs;

namespace SnakeGame
{
    public class Renderer
    {
        private int _screenWidth;
        private int _screenHeight;
        private int _gridSize;

        public Renderer(int w, int h, int grid)
        {
            _screenWidth = w;
            _screenHeight = h;
            _gridSize = grid;
        }

        public void DrawGame(Snake snake, CustomLinkedList<GameElement> elements, List<Particle> particles, Level level, int score)
        {
            // Fondo dinámico según nivel (cambia ligeramente el tono)
            int blueVal = 50 + (level.Number * 10);
            if (blueVal > 200) blueVal = 200;
            Raylib.ClearBackground(new Color(20, 20, blueVal, 255));

            // Dibujar partículas (Requisito 12)
            foreach (var p in particles)
            {
                Color pCol = p.Color;
                pCol.A = (byte)(p.Life * 255);
                Raylib.DrawCircleV(p.Position, 3 + (p.Life * 2), pCol);
            }

            // Dibujar Elementos (Comida/Trampas)
            foreach (var el in elements)
            {
                if (el.Type == ElementType.Food)
                {
                    Raylib.DrawCircle((int)el.Position.X + _gridSize/2, (int)el.Position.Y + _gridSize/2, _gridSize/2 - 2, Color.Green);
                }
                else if (el.Type == ElementType.Trap)
                {
                    Raylib.DrawCircle((int)el.Position.X + _gridSize/2, (int)el.Position.Y + _gridSize/2, _gridSize/2 - 2, Color.Red);
                    Raylib.DrawText("X", (int)el.Position.X + 6, (int)el.Position.Y + 4, 15, Color.White);
                }
            }

            // Dibujar Serpiente
            int index = 0;
            foreach (var segment in snake.Body)
            {
                if (index == 0) // Cabeza
                {
                    Raylib.DrawRectangle((int)segment.X, (int)segment.Y, _gridSize, _gridSize, Color.Red);
                    // Ojos simples
                    Raylib.DrawCircle((int)segment.X + 5, (int)segment.Y + 5, 2, Color.White);
                    Raylib.DrawCircle((int)segment.X + 15, (int)segment.Y + 5, 2, Color.White);
                }
                else // Cuerpo
                {
                    Raylib.DrawRectangle((int)segment.X + 1, (int)segment.Y + 1, _gridSize - 2, _gridSize - 2, Color.Lime);
                }
                index++;
            }

            // HUD
            Raylib.DrawRectangle(0, 0, _screenWidth, 30, new Color(0, 0, 0, 150));
            Raylib.DrawText($"Nivel: {level.Number}", 10, 5, 20, Color.White);
            Raylib.DrawText($"Tamaño: {snake.Body.Count}", 150, 5, 20, Color.White);
            Raylib.DrawText($"Puntos: {score}", 300, 5, 20, Color.Gold);

            // Efecto Visual Teletransporte (Requisito 12)
            if (snake.JustTeleported)
            {
                Raylib.DrawRectangleLinesEx(new Rectangle(0,0, _screenWidth, _screenHeight), 5, Color.SkyBlue);
            }
        }

        public void DrawMenu()
        {
            Raylib.ClearBackground(Color.RayWhite);
            DrawCenteredText("SNAKE GAME - RAYLIB", -50, 40, Color.DarkGreen);
            DrawCenteredText("Presiona ENTER para Jugar", 20, 20, Color.DarkGray);
            DrawCenteredText("Presiona H para High Scores", 50, 20, Color.DarkGray);
            DrawCenteredText("ESC para Salir", 80, 20, Color.DarkGray);
        }

        public void DrawGameOver(int score, int highScore)
        {
            Raylib.ClearBackground(Color.Black);
            DrawCenteredText("GAME OVER", -50, 40, Color.Red);
            DrawCenteredText($"Puntuación Final: {score}", 10, 20, Color.White);
            DrawCenteredText($"Mejor Puntuación: {highScore}", 40, 20, Color.Gold);
            DrawCenteredText("ENTER: Reiniciar | ESC: Menú", 100, 20, Color.Gray);
        }

        public void DrawLevelComplete(int level, int bonus)
        {
            Raylib.ClearBackground(Color.DarkBlue);
            DrawCenteredText($"¡NIVEL {level} COMPLETADO!", -50, 30, Color.Yellow);
            DrawCenteredText($"Bonus de nivel: +{bonus}", 0, 20, Color.White);
            DrawCenteredText("Presiona ENTER para continuar", 50, 20, Color.Gray);
        }

        public void DrawHighScores(List<ScoreEntry> scores)
        {
            Raylib.ClearBackground(Color.RayWhite);
            DrawCenteredText("MEJORES PUNTUACIONES", -150, 30, Color.DarkBlue);
            
            int yOffset = -80;
            foreach(var s in scores)
            {
                DrawCenteredText($"{s.Date} - {s.Score} pts", yOffset, 20, Color.Black);
                yOffset += 30;
            }

            DrawCenteredText("ESC para Volver", 150, 20, Color.DarkGray);
        }

        private void DrawCenteredText(string text, int offsetY, int fontSize, Color color)
        {
            int textWidth = Raylib.MeasureText(text, fontSize);
            Raylib.DrawText(text, (_screenWidth - textWidth) / 2, (_screenHeight / 2) + offsetY, fontSize, color);
        }
    }
}