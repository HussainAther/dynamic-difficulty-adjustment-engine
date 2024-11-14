# src/difficulty_adjuster.py

class DifficultyAdjuster:
    def __init__(self, metrics_tracker, base_difficulty=1):
        self.metrics_tracker = metrics_tracker
        self.difficulty_level = base_difficulty  # Starting difficulty level

    def adjust_difficulty(self):
        """Adjusts difficulty based on player performance metrics."""
        metrics = self.metrics_tracker.calculate_metrics()
        success_rate = metrics["success_rate"]
        avg_time = metrics["average_time"]

        # Logic to adjust difficulty based on success rate and average time
        if success_rate < 0.5 and avg_time > 10:
            self.increase_difficulty()
        elif success_rate > 0.8 and avg_time < 5:
            self.decrease_difficulty()

    def increase_difficulty(self):
        """Increases the difficulty level."""
        print("Increasing difficulty...")
        self.difficulty_level += 1
        # Additional code for adjusting game parameters

    def decrease_difficulty(self):
        """Decreases the difficulty level."""
        if self.difficulty_level > 1:
            print("Decreasing difficulty...")
            self.difficulty_level -= 1
            # Additional code for adjusting game parameters

    def get_difficulty_level(self):
        """Returns the current difficulty level."""
        return self.difficulty_level

