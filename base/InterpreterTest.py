import ast
import pathlib
import sys
import unittest


class InterpreterTestCase(unittest.TestCase):
    base = pathlib.Path(__file__).parent.parent.resolve().__str__() + '/'

    def abstract_test(self, path):
        test = InterpreterTestCase.base + path
        src_test = InterpreterTestCase.base + '/base/test_src/' + path.replace('/', '_') + '.txt'
        sys.path.append(test)
        sys.path.append(src_test)
        from Interpreter import Interpreter

        with open(src_test, 'r') as f:
            test_pairs = [ast.literal_eval(i) for i in f.readlines()]

        for test, expected in test_pairs:
            with self.subTest(test=test, expected=expected):
                self.assertEqual(Interpreter(test).expr(), expected)

        del sys.modules['Interpreter']
        del sys.modules['Token']
        sys.path.remove(InterpreterTestCase.base + path)

    def test_part1_lesson(self):
        self.abstract_test('part 1 - simple arithmetic interpreter/lesson')

    def test_part1_practice(self):
        self.abstract_test('part 1 - simple arithmetic interpreter/practice')

    def test_part2_lesson(self):
        self.abstract_test('part 2/lesson')

    def test_part2_practice(self):
        self.abstract_test('part 2/practice')

    def test_part3_lesson(self):
        self.abstract_test('part 3/lesson')

    def test_part3_practice(self):
        self.abstract_test('part 3/practice')


if __name__ == '__main__':
    unittest.main()
