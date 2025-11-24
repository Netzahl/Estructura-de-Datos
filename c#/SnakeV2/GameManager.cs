using System;
using System.Numerics;
using System.Collections.Generic;
using System.Linq; // Necesario para Count

using Raylib_cs;

namespace SnakeGame
{
    public class GameManager
    {
        // Constantes
        private const int ScreenWidth = 800;
        private const int ScreenHeight = 600;
        private const int GridSize = 25;
        // Límite de elementos: Max 2 de Comida, Max 2 de Trampa (aunque el spawn de riesgo es aparte)
        private const int MaxFoodElements = 2; 

        // Managers
        private Snake _snake;
        private LevelManager _levelManager;
        private ScoreManager _scoreManager;
        private Renderer _renderer;

        // Estado
        private GameState _state;
        private float _moveTimer;
        
        // Listas personalizadas para elementos (Requisito 3)
        private CustomLinkedList<GameElement> _elements;
        private List<Particle> _particles; 

        public GameManager()
        {
            _snake = new Snake(ScreenWidth / 2, ScreenHeight / 2, GridSize, ScreenWidth, ScreenHeight);
            _levelManager = new LevelManager();
            _scoreManager = new ScoreManager();
            _renderer = new Renderer(ScreenWidth, ScreenHeight, GridSize);
            _elements = new CustomLinkedList<GameElement>();
            _particles = new List<Particle>();
            _state = GameState.Menu;
            
            SetupInitialElements();
        }
        
        private void SetupInitialElements()
        {
            _elements.Clear();
            SpawnElement(ElementType.Food);
            // La trampa inicial no está sujeta al % de riesgo, solo al límite de MaxFoodElements
            SpawnElement(ElementType.Trap); 
        }

        public void Run()
        {
            Raylib.InitWindow(ScreenWidth, ScreenHeight, "Snake Game - Raylib");
            Raylib.SetTargetFPS(60);

            while (!Raylib.WindowShouldClose())
            {
                Update();
                Draw();
            }

            Raylib.CloseWindow();
        }

        private void Update()
        {
            switch (_state)
            {
                case GameState.Menu:
                    if (Raylib.IsKeyPressed(KeyboardKey.Enter)) StartGame();
                    if (Raylib.IsKeyPressed(KeyboardKey.H)) _state = GameState.HighScores;
                    if (Raylib.IsKeyPressed(KeyboardKey.Escape)) Raylib.CloseWindow(); // Salir de la aplicación
                    break;

                case GameState.HighScores:
                    if (Raylib.IsKeyPressed(KeyboardKey.Escape)) _state = GameState.Menu;
                    break;

                case GameState.Playing:
                    HandleInput();
                    UpdateGameplay();
                    break;

                case GameState.LevelComplete:
                    if (Raylib.IsKeyPressed(KeyboardKey.Enter)) NextLevel();
                    break;

                case GameState.GameOver:
                    // SOLUCIÓN AL BUG DE ESC: Solo cambiamos el estado a Menu. 
                    // Si el usuario quiere salir del juego, tiene que volver al Menu y presionar ESC de nuevo.
                    if (Raylib.IsKeyPressed(KeyboardKey.Enter)) StartGame();
                    if (Raylib.IsKeyPressed(KeyboardKey.Escape)) _state = GameState.Menu; 
                    break;
            }

            UpdateParticles();
        }

        private void StartGame()
        {
            _snake.Reset(ScreenWidth / 2, ScreenHeight / 2);
            _levelManager.Reset();
            _scoreManager.ResetScore();
            _elements.Clear();
            _particles.Clear();
            SetupInitialElements(); // Generar comida y trampa
            _state = GameState.Playing;
        }

        private void HandleInput()
        {
            if (Raylib.IsKeyPressed(KeyboardKey.Up)) _snake.UpdateDirection(new Vector2(0, -1));
            if (Raylib.IsKeyPressed(KeyboardKey.Down)) _snake.UpdateDirection(new Vector2(0, 1));
            if (Raylib.IsKeyPressed(KeyboardKey.Left)) _snake.UpdateDirection(new Vector2(-1, 0));
            if (Raylib.IsKeyPressed(KeyboardKey.Right)) _snake.UpdateDirection(new Vector2(1, 0));
            
            // Pausa (va al menú)
            if (Raylib.IsKeyPressed(KeyboardKey.Space) || Raylib.IsKeyPressed(KeyboardKey.Escape)) 
            {
                _state = GameState.Menu; 
            }
        }

        private void UpdateGameplay()
        {
            _moveTimer += Raylib.GetFrameTime();
            if (_moveTimer >= _levelManager.CurrentLevel.Speed)
            {
                _moveTimer = 0;
                
                bool grow = CheckCollisions(out bool hitTrap);
                
                if (hitTrap) 
                {
                    _snake.Shrink();
                    CreateParticles(_snake.Body.Head!.Data, Color.Red);
                }

                _snake.Move(grow);

                if (_snake.CheckSelfCollision() || _snake.Body.Count == 0)
                {
                    GameOver();
                }

                if (_snake.Body.Count >= 15)
                {
                    LevelComplete();
                }
            }
        }

        private bool CheckCollisions(out bool hitTrap)
        {
            hitTrap = false;
            Vector2 head = _snake.Body.Head!.Data;
            Vector2 collisionPos = head; 
            
            bool consumedElement = false;
            GameElement? elementToConsume = null;

            // Busca el elemento chocado (ineficiencia O(n) de la CustomLinkedList)
            foreach (var el in _elements)
            {
                 // Usamos Distance en lugar de == para mayor robustez en Raylib
                 if (Vector2.Distance(collisionPos, el.Position) < GridSize/2) 
                 {
                    elementToConsume = el;
                    consumedElement = true;
                    break;
                 }
            }

            if (consumedElement && elementToConsume != null)
            {
                ElementType type = elementToConsume.Type;

                // 1. Eliminar SÓLO el elemento consumido de la CustomLinkedList
                _elements.Remove(elementToConsume); 
                
                // 2. Lógica del elemento
                if (type == ElementType.Food)
                {
                    _scoreManager.AddScore(10 * _levelManager.CurrentLevel.Number);
                    hitTrap = false; 
                    CreateParticles(collisionPos, Color.Green);
                    
                    // Lógica de reemplazo y riesgo:
                    SpawnNewFoodIfMissing(); // Reemplazar la comida consumida (Lógica 1:1)
                    AttemptSpawnTrapOnFood(); // Evaluar la aparición de una NUEVA trampa (Lógica de Riesgo)
                    
                    return true; // Crecer
                }
                else if (type == ElementType.Trap)
                {
                    hitTrap = true;
                    CreateParticles(collisionPos, Color.Red);
                    
                    // Lógica de reemplazo:
                    SpawnNewTrapIfMissing(); // Reemplazar la trampa consumida (Lógica 1:1)
                    
                    return false; // No crecer
                }
            }
            return false;
        }

        /// <summary>
        /// Intenta generar una trampa basada en el porcentaje dinámico del nivel.
        /// (Objetivo 1) - Esta lógica es independiente de la cantidad actual de trampas.
        /// </summary>
        private void AttemptSpawnTrapOnFood()
        {
            float chance = _levelManager.GetDynamicTrapSpawnChance();
            float roll = Raylib.GetRandomValue(0, 100) / 100.0f; // 0.0 a 1.0

            if (roll < chance)
            {
                // Solo generamos una trampa si la tirada es menor que la probabilidad.
                SpawnElement(ElementType.Trap);
            }
        }
        
        /// <summary>
        /// Genera una nueva comida si el conteo actual es menor que el máximo permitido.
        /// </summary>
        private void SpawnNewFoodIfMissing()
        {
            int foodCount = 0;
            foreach (var el in _elements)
            {
                if (el.Type == ElementType.Food) foodCount++;
            }
            
            if (foodCount < MaxFoodElements)
            {
                SpawnElement(ElementType.Food);
            }
        }
        
        /// <summary>
        /// Genera una nueva trampa si el conteo actual es menor que el máximo permitido.
        /// (Lógica de reemplazo simple, no ligada al riesgo).
        /// </summary>
        private void SpawnNewTrapIfMissing()
        {
            int trapCount = 0;
            foreach (var el in _elements)
            {
                if (el.Type == ElementType.Trap) trapCount++;
            }
            
            if (trapCount < MaxFoodElements)
            {
                // Solo generamos una trampa de reemplazo si el conteo es menor al límite.
                SpawnElement(ElementType.Trap);
            }
        }

        private void SpawnElement(ElementType type)
        {
            int cols = ScreenWidth / GridSize;
            int rows = ScreenHeight / GridSize;
            Vector2 pos;
            bool occupied;

            do
            {
                pos = new Vector2(
                    Raylib.GetRandomValue(0, cols - 1) * GridSize,
                    Raylib.GetRandomValue(0, rows - 1) * GridSize
                );
                
                occupied = false;
                
                // Chequear cuerpo de la serpiente
                foreach (var segment in _snake.Body)
                {
                    if (segment == pos)
                    {
                        occupied = true;
                        break;
                    }
                }
                
                // Chequear otros elementos
                if (!occupied)
                {
                    foreach (var el in _elements)
                    {
                        if (el.Position == pos)
                        {
                            occupied = true;
                            break;
                        }
                    }
                }

            } while (occupied);
            
            _elements.Add(new GameElement(pos, type));
        }

        private void CreateParticles(Vector2 pos, Color color)
        {
            for(int i=0; i<10; i++) _particles.Add(new Particle(pos, color));
        }

        private void UpdateParticles()
        {
            for (int i = _particles.Count - 1; i >= 0; i--)
            {
                _particles[i].Position += _particles[i].Velocity;
                _particles[i].Life -= 0.05f;
                if (_particles[i].Life <= 0) _particles.RemoveAt(i);
            }
        }

        private void LevelComplete()
        {
            _state = GameState.LevelComplete;
            int bonus = 100 * _levelManager.CurrentLevel.Number;
            _scoreManager.AddScore(bonus);
        }

        private void NextLevel()
        {
            _levelManager.AdvanceLevel();
            _snake.Reset(ScreenWidth/2, ScreenHeight/2);
            _elements.Clear();
            SetupInitialElements(); // Generar la base de comida y trampa
            _state = GameState.Playing;
        }

        private void GameOver()
        {
            _state = GameState.GameOver;
            _scoreManager.SaveCurrentScore();
        }

        private void Draw()
        {
            Raylib.BeginDrawing();
            Raylib.ClearBackground(Color.Black);
            
            switch (_state)
            {
                case GameState.Menu: _renderer.DrawMenu(); break;
                case GameState.Playing: _renderer.DrawGame(_snake, _elements, _particles, _levelManager.CurrentLevel, _scoreManager.CurrentScore); break;
                case GameState.LevelComplete: _renderer.DrawLevelComplete(_levelManager.CurrentLevel.Number, 100 * _levelManager.CurrentLevel.Number); break;
                case GameState.GameOver: _renderer.DrawGameOver(_scoreManager.CurrentScore, _scoreManager.HighScore); break;
                case GameState.HighScores: _renderer.DrawHighScores(_scoreManager.HighScores); break;
            }

            Raylib.EndDrawing();
        }
    }
}