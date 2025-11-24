namespace SnakeGameRaylib
{
    public class ScoreManager
    {
        public int Score { get; private set; }

        public void AddScore(int amount)
        {
            Score += amount;
        }

        public void Reset() => Score = 0;
    }
}
