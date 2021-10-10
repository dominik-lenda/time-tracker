import unittest
import timetracker

class TestTimeTracker(unittest.TestCase):

  def test_time_tracker(self):
    result = timetracker.time_tracker(2, 3)
    self.assertEqual(result, 1)