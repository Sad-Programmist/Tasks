import unittest
from task_4 import *


class MyTestCase(unittest.TestCase):
    def test_01(self):
        text, words = read("input files/input1.txt")
        output = correction(text, words)
        correct = "Один два три чатырэ пятью"
        self.assertEqual(output, correct)

    def test_02(self):
        text, words = read("input files/input2.txt")
        output = correction(text, words)
        correct = "Привет Яна, как дела?"
        self.assertEqual(output, correct)

    def test_03(self):
        text, words = read("input files/input3.txt")
        output = correction(text, words)
        correct = "Атлечный ризультот палучився"
        self.assertEqual(output, correct)

    def test_04(self):
        text, words = read("input files/input4.txt")
        output = correction(text, words)
        correct = "На лесной опушке распускаются колоколчики, незабудки, шиповник."
        self.assertEqual(output, correct)

    def test_05(self):
        text, words = read("input files/input5.txt")
        output = correction(text, words)
        correct = "Однажды к старому ежу подбежала собака."
        self.assertEqual(output, correct)


if __name__ == '__main__':
    unittest.main()
