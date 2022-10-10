import unittest
import sys
from io import StringIO
from Interpreter import Interpreter


class InterpreterTestCase(unittest.TestCase):
    test_pairs_begin = [
        ('3+5', 8),
        ('3+4', 7),
        ('3+9', 12),
    ]

    def test(self):
        for text, expected in InterpreterTestCase.test_pairs_begin:
            with self.subTest(text=text, expected=expected):
                self.assertEqual(Interpreter(text).expr(), expected)


if __name__ == '__main__':
    unittest.main()
