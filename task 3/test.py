import unittest
from task_3 import *


class MyTestCase(unittest.TestCase):
    def test_01(self):
        output = one_quarter("input files/input1.txt")
        correct = []
        self.assertEqual(output, correct)

    def test_02(self):
        output = one_quarter("input files/input2.txt")
        correct = []
        self.assertEqual(output, correct)

    def test_03(self):
        output = one_quarter("input files/input3.txt")
        correct = []
        self.assertEqual(output, correct)

    def test_04(self):
        output = one_quarter("input files/input4.txt")
        correct = [Triangle(1, 1, 2, 5, 6, 7), Triangle(-1, -1, -2, -5, -6, -7),
                   Triangle(-1, 1, -2, 5, -6, 7), Triangle(1, -1, 2, -5, 6, -7)]
        self.assertEqual(output, correct)

    def test_05(self):
        with self.assertRaises(ValueError):
            one_quarter("input files/input5.txt")


if __name__ == '__main__':
    unittest.main()
