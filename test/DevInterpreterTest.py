import unittest

from TestMethods import TestMethods


class DevInterpreterTestCase(TestMethods):
    def test_part9_lesson(self):
        self.abstract_program_test('part 9 - simple program/lesson')

    def test_part9_practice(self):
        self.abstract_program_test('part 9 - simple program/practice')

    def test_part10_lesson(self):
        self.abstract_program_test('part 10 - complete program/lesson')

    def test_part11_lesson(self):
        self.abstract_program_test('part 11 - symbol tables/lesson')

    def test_part12_lesson(self):
        self.abstract_program_test('part 12 - procedures/lesson')


if __name__ == '__main__':
    unittest.main()
