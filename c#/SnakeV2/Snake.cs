using System.Numerics;
using Raylib_cs;

namespace SnakeGame
{
    public class Snake
    {
        // Requisito 3: Usar listas de nodos para el cuerpo
        public CustomLinkedList<Vector2> Body { get; private set; }
        public Vector2 Direction { get; set; }
        public Vector2 NextDirection { get; set; } // Buffer para evitar giros de 180 en 1 frame
        
        private int _gridSize;
        private int _screenWidth;
        private int _screenHeight;
        public bool JustTeleported { get; private set; }

        public Snake(int startX, int startY, int gridSize, int screenW, int screenH)
        {
            Body = new CustomLinkedList<Vector2>();
            _gridSize = gridSize;
            _screenWidth = screenW;
            _screenHeight = screenH;
            Reset(startX, startY);
        }

        public void Reset(int startX, int startY)
        {
            Body.Clear();
            // Requisito 5: Tamaño inicial 5 segmentos
            for (int i = 0; i < 5; i++)
            {
                Body.Add(new Vector2(startX - (i * _gridSize), startY));
            }
            Direction = new Vector2(1, 0); // Derecha
            NextDirection = new Vector2(1, 0);
        }

        public void UpdateDirection(Vector2 newDir)
        {
            // Evitar giro de 180 grados directo
            if ((Direction.X + newDir.X != 0) || (Direction.Y + newDir.Y != 0))
            {
                NextDirection = newDir;
            }
        }

        /// <summary>
        /// Mueve la serpiente y maneja la LÓGICA DE TELETRANSPORTE (Requisito 2 y 15)
        /// </summary>
        public void Move(bool grow)
        {
            Direction = NextDirection;
            Vector2 head = Body.Head!.Data;
            Vector2 newHead = head + (Direction * _gridSize);
            JustTeleported = false;

            // --- LÓGICA DE TELETRANSPORTE (WRAP-AROUND) ---
            // Si sale por la derecha (>= ancho), aparece en 0
            if (newHead.X >= _screenWidth) 
            {
                newHead.X = 0;
                JustTeleported = true;
            }
            // Si sale por la izquierda (< 0), aparece en ancho - grid
            else if (newHead.X < 0) 
            {
                newHead.X = _screenWidth - _gridSize;
                JustTeleported = true;
            }
            // Si sale por abajo (>= alto), aparece en 0
            else if (newHead.Y >= _screenHeight) 
            {
                newHead.Y = 0;
                JustTeleported = true;
            }
            // Si sale por arriba (< 0), aparece en alto - grid
            else if (newHead.Y < 0) 
            {
                newHead.Y = _screenHeight - _gridSize;
                JustTeleported = true;
            }
            // ---------------------------------------------

            Body.AddFirst(newHead);

            if (!grow)
            {
                Body.RemoveLast();
            }
        }

        public void Shrink()
        {
            if (Body.Count > 0)
            {
                Body.RemoveLast();
            }
        }

        public bool CheckSelfCollision()
        {
            Vector2 head = Body.Head!.Data;
            int index = 0;
            foreach (var segment in Body)
            {
                if (index > 0 && segment.X == head.X && segment.Y == head.Y)
                {
                    return true;
                }
                index++;
            }
            return false;
        }
    }
}