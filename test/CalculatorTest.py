import unittest

from TestMethods import TestMethods


class CalculatorTestCase(TestMethods):
    def test_part1_lesson(self):
        self.abstract_calc_test('part 1 - simple arithmetic interpreter/lesson')

    def test_part1_practice(self):
        self.abstract_calc_test('part 1 - simple arithmetic interpreter/practice')

    def test_part2_lesson(self):
        self.abstract_calc_test('part 2/lesson')

    def test_part2_practice(self):
        self.abstract_calc_test('part 2/practice')

    def test_part3_lesson(self):
        self.abstract_calc_test('part 3/lesson')

    def test_part3_practice(self):
        self.abstract_calc_test('part 3/practice')

    def test_part4_lesson(self):
        self.abstract_calc_test('part 4/lesson')

    def test_part4_practice(self):
        self.abstract_calc_test('part 4/practice')

    def test_part5_lesson(self):
        self.abstract_calc_test('part 5 - operators precedence/lesson')

    def test_part5_practice(self):
        self.abstract_calc_test('part 5 - operators precedence/practice')

    def test_part6_lesson(self):
        self.abstract_calc_test('part 6/lesson')

    def test_part7_lesson(self):
        self.abstract_calc_test('part 7 - AST/lesson')

    def test_part7_practice(self):
        self.abstract_calc_test('part 7 - AST/practice')

    def test_part8_lesson(self):
        self.abstract_calc_test('part 8 - unary operators/lesson')


if __name__ == '__main__':
    unittest.main()
