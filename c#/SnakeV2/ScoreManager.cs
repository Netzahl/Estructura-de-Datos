using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.Json;

namespace SnakeGame
{
    public class ScoreEntry
    {
        public string Date { get; set; } = "";
        public int Score { get; set; }
    }

    public class ScoreManager
    {
        public int CurrentScore { get; private set; }
        public int HighScore { get; private set; }
        private string _filePath = "highscores.json";
        public List<ScoreEntry> HighScores { get; private set; }

        public ScoreManager()
        {
            CurrentScore = 0;
            HighScores = new List<ScoreEntry>();
            LoadScores();
        }

        public void AddScore(int amount)
        {
            CurrentScore += amount;
            if (CurrentScore > HighScore) HighScore = CurrentScore;
        }

        public void ResetScore()
        {
            CurrentScore = 0;
        }

        public void SaveCurrentScore()
        {
            HighScores.Add(new ScoreEntry { Date = DateTime.Now.ToString("yyyy-MM-dd HH:mm"), Score = CurrentScore });
            // Top 5
            HighScores = HighScores.OrderByDescending(x => x.Score).Take(5).ToList();
            SaveToFile();
        }

        private void SaveToFile()
        {
            try
            {
                string json = JsonSerializer.Serialize(HighScores);
                File.WriteAllText(_filePath, json);
            }
            catch { /* Ignorar errores de IO en demo */ }
        }

        private void LoadScores()
        {
            try
            {
                if (File.Exists(_filePath))
                {
                    string json = File.ReadAllText(_filePath);
                    HighScores = JsonSerializer.Deserialize<List<ScoreEntry>>(json) ?? new List<ScoreEntry>();
                    if (HighScores.Count > 0)
                        HighScore = HighScores.Max(x => x.Score);
                }
            }
            catch { HighScores = new List<ScoreEntry>(); }
        }
    }
}