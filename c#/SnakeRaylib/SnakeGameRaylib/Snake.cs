using System.Collections.Generic;
using System.Numerics;

namespace SnakeGameRaylib
{
    public class Snake
    {
        public List<Vector2> Body { get; private set; } = new List<Vector2>();
        public Vector2 Direction { get; set; }

        public int SegmentSize { get; } = 20;

        public Snake()
        {
            // Inicializar snake centrada
            Direction = new Vector2(SegmentSize, 0);
            Body.Clear();
            var startX = 200;
            var startY = 200;
            // tamaño inicial 5
            for (int i = 0; i < 5; i++)
            {
                Body.Add(new Vector2(startX - i * SegmentSize, startY));
            }
        }

        public void Move()
        {
            // mover cuerpo hacia adelante
            for (int i = Body.Count - 1; i > 0; i--)
            {
                Body[i] = Body[i - 1];
            }

            // nueva cabeza
            Body[0] = new Vector2(Body[0].X + Direction.X, Body[0].Y + Direction.Y);
        }

        public void Grow()
        {
            // añadir un segmento en la posición del último segmento
            Body.Add(Body[Body.Count - 1]);
        }

        public void Shrink()
        {
            if (Body.Count > 0) Body.RemoveAt(Body.Count - 1);
        }
    }
}
