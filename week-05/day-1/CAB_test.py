import unittest
import CAB

class CAB_game_test(unittest.TestCase):

    def test_guess_result_everything_fit(self):
        self.assertEqual(CAB.__init__(), 4567)
