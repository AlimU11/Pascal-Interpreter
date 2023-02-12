import unittest

from TestMethods import TestMethods


class DevInterpreterTestCase(TestMethods):
    def test_part9_lesson(self):
        self.abstract_program_test('part 9 - simple program/lesson')

    def test_part9_practice(self):
        self.abstract_program_test('part 9 - simple program/practice')

    def test_part_10_lesson(self):
        self.abstract_program_test('part 10 - complete program/lesson')

    def test_part_11_lesson(self):
        self.abstract_program_test('part 11 - symbol tables/lesson')

    def test_part_12_lesson(self):
        self.abstract_program_test('part 12 - procedures/lesson')

    def test_part_13_lesson(self):
        self.import_modules('part 13 - semantic analysis/lesson')
        self.abstract_test_fail('part 13 - semantic analysis_lesson.pas')


if __name__ == '__main__':
    unittest.main()
