import ast
import pathlib
import sys
import unittest


class TestMethods(unittest.TestCase):
    base = pathlib.Path(__file__).parent.parent.resolve().__str__() + '/'

    def import_modules(self, path):
        test = TestMethods.base + path
        src_test = TestMethods.base + '/test/test_src/' + path.replace('/', '_') + '.txt'
        sys.path.append(test)
        sys.path.append(src_test)

        return src_test

    def delete(self, path):
        if 'Interpreter' in sys.modules:
            del sys.modules['Interpreter']

        if 'Token' in sys.modules:
            del sys.modules['Token']

        if 'Lexer' in sys.modules:
            del sys.modules['Lexer']

        if 'Parser' in sys.modules:
            del sys.modules['Parser']

        if 'Node' in sys.modules:
            del sys.modules['Node']

        if 'AST' in sys.modules:
            del sys.modules['AST']

        if 'SymbolTable' in sys.modules:
            del sys.modules['SymbolTable']

        if 'Symbol' in sys.modules:
            del sys.modules['Symbol']

        if 'NodeVisitor' in sys.modules:
            del sys.modules['NodeVisitor']

        if 'SemanticAnalyzer' in sys.modules:
            del sys.modules['SemanticAnalyzer']

        if 'ScopedSymbolTable' in sys.modules:
            del sys.modules['ScopedSymbolTable']

        if 'Error' in sys.modules:
            del sys.modules['Error']

        if 'ARType' in sys.modules:
            del sys.modules['ARType']

        if 'ActivationRecord' in sys.modules:
            del sys.modules['ActivationRecord']

        if 'ARTree' in sys.modules:
            del sys.modules['ARTree']

        if 'ARNode' in sys.modules:
            del sys.modules['ARNode']

        if 'CallStack' in sys.modules:
            del sys.modules['CallStack']

        if 'TokenType' in sys.modules:
            del sys.modules['TokenType']

        sys.path.remove(TestMethods.base + path)

    def abstract_calc_test(self, path):
        src_test = self.import_modules(path)

        from Interpreter import Interpreter

        with open(src_test, 'r') as f:
            test_pairs = [ast.literal_eval(i) for i in f.readlines()]

        for test, expected in test_pairs:
            with self.subTest(test=test, expected=expected):
                self.assertEqual(Interpreter(test).expr(), expected)

        self.delete(path)

    def abstract_program_test(self, path, test_scopes=False):
        src_test = self.import_modules(path)
        src_program = TestMethods.base + 'test/test_src/' + path.replace('/', '_') + '.pas'

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        with open(src_test, 'r') as f:
            global_scope = ast.literal_eval(f.read())

        interpreter = Interpreter(program)
        interpreter.interpret()

        self.assertEqual(
            (
                interpreter.GLOBAL_SCOPE
                if not test_scopes
                else [
                    [
                        scope.scope_name,
                        scope.scope_level,
                        scope.enclosing_scope.scope_name if scope.enclosing_scope else None,
                    ]
                    for scope in interpreter.semantic_analyzer.scopes
                ]
            ),
            global_scope,
        )
        self.delete(path)

    def abstract_test_pass(self, path, path_suffix=''):
        self.import_modules(path)
        src_program = TestMethods.base + 'test/test_src/' + path.replace('/', '_') + path_suffix + '.pas'

        if not 'base' in path:
            from Interpreter import Interpreter
        else:
            import base
            from base.Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        interpreter = Interpreter(program)
        interpreter.interpret()

        self.delete(path)

    def abstract_test_fail(self, path, path_suffix: str = '', exception=Exception):
        self.import_modules(path)
        src_program = TestMethods.base + 'test/test_src/' + path.replace('/', '_') + path_suffix + '.pas'

        from Interpreter import Interpreter

        with open(src_program, 'r') as f:
            program = f.read()

        interpreter = Interpreter(program)

        if isinstance(exception, str):
            exception = getattr(sys.modules['Error'], exception)

        with self.assertRaises(exception):
            interpreter.interpret()

        self.delete(path)
