using System.Numerics;

namespace SnakeGameRaylib
{
    public class GameElement
    {
        public enum ElementType { Food, Trap }

        public ElementType Type { get; set; }
        public Vector2 Position { get; set; }
        public float Radius { get; set; }

        public GameElement(ElementType type, Vector2 position, float radius)
        {
            Type = type;
            Position = position;
            Radius = radius;
        }
    }
}
