using System.Numerics;
using Raylib_cs;

namespace SnakeGame
{
    public class GameElement
    {
        public Vector2 Position { get; set; }
        public ElementType Type { get; set; }
        public bool IsActive { get; set; } = true;

        public GameElement(Vector2 pos, ElementType type)
        {
            Position = pos;
            Type = type;
        }
    }

    // Clase simple para partículas visuales
    public class Particle
    {
        public Vector2 Position;
        public Vector2 Velocity;
        public Color Color;
        public float Life; // 1.0f a 0.0f

        public Particle(Vector2 pos, Color col)
        {
            Position = pos;
            Color = col;
            Velocity = new Vector2(Raylib.GetRandomValue(-2, 2), Raylib.GetRandomValue(-2, 2));
            Life = 1.0f;
        }
    }
}