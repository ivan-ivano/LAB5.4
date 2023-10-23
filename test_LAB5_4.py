import unittest
from LAB5_4 import P1


class TestP1(unittest.TestCase):
    def test_P1(self):
        self.assertEqual(P1(1,1), 26214.400000000012)  # add assertion here


if __name__ == '__main__':
    unittest.main()
