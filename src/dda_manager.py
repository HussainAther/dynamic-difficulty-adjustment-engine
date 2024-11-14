# src/dda_manager.py

import time
from metrics_tracker import MetricsTracker
from difficulty_adjuster import DifficultyAdjuster

class DDAEngine:
    def __init__(self):
        self.metrics_tracker = MetricsTracker()
        self.difficulty_adjuster = DifficultyAdjuster(self.metrics_tracker)

    def run_game_loop(self):
        """Simulates a game loop with dynamic difficulty adjustment."""
        while True:
            task_start_time = time.time()
            success, error = self.simulate_task()  # Simulate player task
            task_time = time.time() - task_start_time

            # Track success or failure based on task result
            if success:
                self.metrics_tracker.record_success(task_time)
            else:
                self.metrics_tracker.record_failure(error, task_time)

            # Adjust difficulty after each task
            self.difficulty_adjuster.adjust_difficulty()
            print("Current Difficulty Level:", self.difficulty_adjuster.get_difficulty_level())

    def simulate_task(self):
        """Placeholder for game logic. Returns success status and error message if any."""
        # For demonstration, this randomly returns success or failure
        import random
        success = random.choice([True, False])
        error = "Example error" if not success else None
        return success, error

