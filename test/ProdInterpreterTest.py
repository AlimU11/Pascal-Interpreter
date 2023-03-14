import unittest

from TestMethods import TestMethods


class ProdInterpreterTestCase(TestMethods):
    def test_case_insensitivity(self):
        self.import_modules('base')
        self.abstract_test_pass(path='', path_suffix='base/pas/case_insensitivity')

    def test_comments(self):
        self.import_modules('base')
        self.abstract_test_pass(path='', path_suffix='base/pas/comments')

    def test_underscore_in_id(self):
        self.import_modules('base')
        self.abstract_test_pass(path='', path_suffix='base/pas/underscore_in_id')

    def test_called_before_declaration_error(self):
        self.import_modules('base')
        self.abstract_test_fail(path='', path_suffix='base/pas/called_before_declaration')

    def test_not_declared_error(self):
        self.import_modules('base')
        self.abstract_test_fail(path='', path_suffix='base/pas/not_declared')

    def test_redeclaration_error(self):
        self.import_modules('base')
        self.abstract_test_fail(path='', path_suffix='base/pas/redeclaration')


if __name__ == '__main__':
    unittest.main()
