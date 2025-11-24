using Raylib_cs;
using System.Numerics;

namespace SnakeGameRaylib
{
    public class GameManager
    {
        private const int screenWidth = 800;
        private const int screenHeight = 600;

        private Snake snake;
        private LevelManager level;
        private ScoreManager score;
        private InputHandler input;
        private Renderer renderer;

        private GameState state = GameState.Playing;

        public GameManager()
        {
            snake = new Snake();
            level = new LevelManager();
            score = new ScoreManager();
            input = new InputHandler();
            renderer = new Renderer();
        }

        public void Run()
        {
            Raylib.InitWindow(screenWidth, screenHeight, "Snake Game - Raylib");
            Raylib.SetTargetFPS(10);

            level.GenerateElements();

            while (!Raylib.WindowShouldClose())
            {
                Update();
                renderer.Draw(snake, level, score);

                if (state == GameState.GameOver)
                {
                    // Mensaje simple
                    Raylib.BeginDrawing();
                    Raylib.DrawText("GAME OVER - Press Enter to restart", 150, 250, 20, Color.Yellow);
                    Raylib.EndDrawing();

                    if (input.IsConfirmPressed())
                    {
                        Restart();
                    }
                }
            }

            Raylib.CloseWindow();
        }

        private void Update()
        {
            if (state != GameState.Playing) return;

            input.HandleInput(snake);
            snake.Move();

            CheckCollisions();
            CheckSelfCollision();
        }

        private void CheckCollisions()
        {
            // colisiones simples con elementos
            for (int i = level.Elements.Count - 1; i >= 0; i--)
            {
                var el = level.Elements[i];
                float dist = Vector2.Distance(snake.Body[0], el.Position);
                if (dist < (snake.SegmentSize / 2f + el.Radius))
                {
                    if (el.Type == GameElement.ElementType.Food)
                    {
                        snake.Grow();
                        score.AddScore(10);
                        level.GenerateElements();
                    }
                    else // Trap
                    {
                        // como ejemplo: gameover por trampa
                        state = GameState.GameOver;
                    }
                }
            }
        }

        private void CheckSelfCollision()
        {
            var head = snake.Body[0];
            for (int i = 1; i < snake.Body.Count; i++)
            {
                if (snake.Body[i].Equals(head))
                {
                    state = GameState.GameOver;
                    break;
                }
            }
        }

        private void Restart()
        {
            snake = new Snake();
            score.Reset();
            level.GenerateElements();
            state = GameState.Playing;
        }
    }
}
