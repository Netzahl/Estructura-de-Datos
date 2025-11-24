using Raylib_cs;
using System.Numerics;

namespace SnakeGameRaylib
{
    public class Renderer
    {
        private float time = 0f;

        public void Draw(Snake snake, LevelManager level, ScoreManager score)
        {
            time += Raylib.GetFrameTime();

            // color de fondo dinámico
            float t = (float)((System.Math.Sin(time * 1.0f) + 1) * 0.5f);

            Color bg = new Color(
                (int)(20 + 200 * t),
                (int)(20 + 120 * (1 - t)),
                (int)(50 + 150 * (1 - t)),
                255
            );

            Raylib.BeginDrawing();
            Raylib.ClearBackground(bg);

            // dibujar serpiente (cabeza roja, cuerpo verde)
            for (int i = 0; i < snake.Body.Count; i++)
            {
                var p = snake.Body[i];
                var color = (i == 0) ? Color.Red : Color.Green;
                Raylib.DrawRectangle((int)p.X, (int)p.Y, snake.SegmentSize, snake.SegmentSize, color);
            }

            // dibujar elementos
            foreach (var el in level.Elements)
            {
                if (el.Type == GameElement.ElementType.Food)
                {
                    Raylib.DrawCircle((int)el.Position.X, (int)el.Position.Y, el.Radius, Color.Green);
                }
                else
                {
                    Raylib.DrawCircle((int)el.Position.X, (int)el.Position.Y, el.Radius, Color.Red);
                    // X blanca
                    Raylib.DrawLine((int)(el.Position.X - el.Radius), (int)(el.Position.Y - el.Radius),
                                    (int)(el.Position.X + el.Radius), (int)(el.Position.Y + el.Radius), Color.White);
                    Raylib.DrawLine((int)(el.Position.X + el.Radius), (int)(el.Position.Y - el.Radius),
                                    (int)(el.Position.X - el.Radius), (int)(el.Position.Y + el.Radius), Color.White);
                }
            }

            // HUD
            Raylib.DrawText($"Score: {score.Score}", 10, 10, 20, Color.White);

            Raylib.EndDrawing();
        }
    }
}
