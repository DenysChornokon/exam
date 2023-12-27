import unittest
from main import ArithmeticProgression


class TestArithmeticProgression(unittest.TestCase):

    def test_nth_term(self):
        progression = ArithmeticProgression(5, 3)
        self.assertEqual(progression.nth_term(1), 5)
        self.assertEqual(progression.nth_term(2), 8)
        self.assertEqual(progression.nth_term(5), 17)
        self.assertEqual(progression.nth_term(10), 32)



if __name__ == "__main__":
    unittest.main()