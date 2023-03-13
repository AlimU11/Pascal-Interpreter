import ast
import os
import unittest

from TestMethods import TestMethods


class ProdInterpreterTestCase(TestMethods):
    def test_results(self):
        file_dir = ProdInterpreterTestCase.base + 'test/test_src/base/'
        src_test = [file_dir + 'txt/' + i for i in os.listdir(file_dir + 'txt') if 'res' in i and i.endswith('.txt')]

        src_program = [file_dir + 'pas/' + i for i in os.listdir(file_dir + 'pas') if 'res' in i and i.endswith('.pas')]

        self.import_modules('base')

        from Interpreter import Interpreter

        for test, program in zip(src_test, src_program):

            test_filename = test.split('/')[-1].split('.')[0]
            program_filename = program.split('/')[-1].split('.')[0]

            with open(test, 'r') as f:
                global_scope = ast.literal_eval(f.read())

            with open(program, 'r') as f:
                program_text = f.read()

            with self.subTest(test=program_filename, expected=test_filename):
                interpreter = Interpreter(program_text)
                interpreter.interpret()
                self.assertEqual(interpreter.GLOBAL_SCOPE, global_scope)

        self.delete('base')

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
