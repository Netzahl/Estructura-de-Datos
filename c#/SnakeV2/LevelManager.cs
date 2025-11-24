using System;
using System.Collections.Generic;

namespace SnakeGame
{
    public class Level
    {
        public int Number { get; private set; }
        public float Speed { get; private set; }
        public float TrapChance { get; private set; }

        public Level(int number, float baseSpeed)
        {
            Number = number;
            // La velocidad se incrementa por nivel (disminuye el intervalo de tiempo)
            Speed = Math.Max(0.05f, baseSpeed - (number * 0.01f)); 
            
            // La probabilidad base de trampa es fija para el nivel, pero la lógica
            // del GameManager ahora usará la nueva propiedad dinámica.
            TrapChance = Math.Min(0.5f, 0.2f + (number * 0.05f)); 
        }
    }

    public class LevelManager
    {
        private float _baseSpeed = 0.2f;
        private int _currentLevelNumber = 1;
        public Level CurrentLevel { get; private set; }

        public LevelManager()
        {
            CurrentLevel = new Level(_currentLevelNumber, _baseSpeed);
        }

        public void AdvanceLevel()
        {
            _currentLevelNumber++;
            CurrentLevel = new Level(_currentLevelNumber, _baseSpeed);
        }

        public void Reset()
        {
            _currentLevelNumber = 1;
            CurrentLevel = new Level(_currentLevelNumber, _baseSpeed);
        }
        
        /// <summary>
        /// Calcula el porcentaje de aparición de trampas al comer Comida, aumentando
        /// con el nivel hasta un máximo del 75%.
        /// </summary>
        public float GetDynamicTrapSpawnChance()
        {
            // Aumenta 5 puntos porcentuales por nivel. Empieza en 5%.
            float chance = 0.05f + (CurrentLevel.Number * 0.05f); 
            // Cap al 75% (0.75f)
            return Math.Min(0.75f, chance); 
        }
    }
}