import unittest
from day1 import *
import random

class Test_test_python_day1(unittest.TestCase):

    def test_twofer(self):
        valid_names = ["clinton", "___", "Kilimangoo", "Valentine", "Python", "one", "me"]
        name = random.choice(valid_names)
        self.assertEqual(twofer(f"{name}"), f"One for {name}, one for me.")

        name = random.choice(valid_names)
        self.assertEqual(twofer(f"{name}"), f"One for {name}, one for me.")

        name = random.choice(valid_names)
        self.assertEqual(twofer(f"{name}"), f"One for {name}, one for me.")

        self.assertEqual(twofer(), f"One for you, one for me.")



if __name__ == '__main__':
    unittest.main()
