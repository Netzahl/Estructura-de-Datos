using Raylib_cs;
using System.Numerics;

namespace SnakeGameRaylib
{
    public class InputHandler
    {
        public void HandleInput(Snake snake)
        {
            // Evitar inversión 180º: sólo cambiar si no es la dirección opuesta
            if (Raylib.IsKeyPressed(KeyboardKey.Up))
            {
                if (snake.Direction.Y == 0) snake.Direction = new Vector2(0, -snake.SegmentSize);
            }
            else if (Raylib.IsKeyPressed(KeyboardKey.Down))
            {
                if (snake.Direction.Y == 0) snake.Direction = new Vector2(0, snake.SegmentSize);
            }
            else if (Raylib.IsKeyPressed(KeyboardKey.Left))
            {
                if (snake.Direction.X == 0) snake.Direction = new Vector2(-snake.SegmentSize, 0);
            }
            else if (Raylib.IsKeyPressed(KeyboardKey.Right))
            {
                if (snake.Direction.X == 0) snake.Direction = new Vector2(snake.SegmentSize, 0);
            }
        }

        public bool IsPausePressed() => Raylib.IsKeyPressed(KeyboardKey.Space);
        public bool IsConfirmPressed() => Raylib.IsKeyPressed(KeyboardKey.Enter);
        public bool IsEscPressed() => Raylib.IsKeyPressed(KeyboardKey.Escape);
        public bool IsHPressed() => Raylib.IsKeyPressed(KeyboardKey.H);
    }
}
