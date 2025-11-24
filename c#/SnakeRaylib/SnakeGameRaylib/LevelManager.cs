using System.Collections.Generic;
using System.Numerics;

namespace SnakeGameRaylib
{
    public class LevelManager
    {
        private readonly List<GameElement> elements = new List<GameElement>();

        public IReadOnlyList<GameElement> Elements => elements.AsReadOnly();

        public void GenerateElements()
        {
            elements.Clear();

            // ejemplo simple: 1 comida, 1 trampa
            elements.Add(new GameElement(GameElement.ElementType.Food, new Vector2(300, 200), 10f));
            elements.Add(new GameElement(GameElement.ElementType.Trap, new Vector2(400, 300), 10f));
        }
    }
}
