import unittest

from Interpreter import Interpreter


class InterpreterTestCase(unittest.TestCase):
    test_pairs_begin = [
        ('3+5', 8),
        ('3+4', 7),
        ('3+9', 12),
        ('12+3', 15),
        ('12 + 3', 15),
        ('7-5', 2),
        ('     3     +   5    ', 8),
        ('3       + 4', 7),
        (' 3+ 4', 7),
        ('3+ 4 ', 7),
        ('9-2', 7),
        ('3-9', -6),
        ('12-3+5', 14),
        ('    12   - 3  + 5  ', 14),
        ('12-3   +5', 14),
        ('5*5   ', 25),
        (' 12 /   3 * 5 ', 20),
    ]

    def test(self):
        for text, expected in InterpreterTestCase.test_pairs_begin:
            with self.subTest(text=text, expected=expected):
                self.assertEqual(Interpreter(text).expr(), expected)


if __name__ == '__main__':
    unittest.main()
