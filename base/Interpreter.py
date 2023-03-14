from base.ActivationRecord import ActivationRecord
from base.ARTree import ARTree
from base.ARType import ARType
from base.CallStack import CallStack
from base.Error import ErrorCode, InterpreterError
from base.NodeVisitor import NodeVisitor
from base.SemanticAnalyzer import SemanticAnalyzer
from base.TokenType import TokenType


class Interpreter(NodeVisitor):
    def __init__(self, text):
        self.MAX_RECURSION_DEPTH = 1000
        self.semantic_analyzer = SemanticAnalyzer(text)
        self.call_stack = CallStack()
        self.ar_tree = ARTree()
        self.global_execution_order = 0

    def error(self, error_code, token):
        raise InterpreterError(error_code, token, message=f'{error_code.value} -> {token}')

    def visit_Program(self, node):
        program_name = node.name

        AR = ActivationRecord(
            name=program_name,
            scope_name='global',
            type=ARType.PROGRAM,
            nesting_level=1,
            execution_order=self.global_execution_order,
            outer_scope=None,
        )

        self.call_stack.push(AR)
        self.global_execution_order += 1

        self.visit(node.block)

        self.ar_tree.push(self.call_stack.pop())

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_VarDecl(self, node):
        # Do nothing
        pass

    def visit_Type(self, node):
        # Do nothing
        pass

    def visit_BinOp(self, node):
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == TokenType.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == TokenType.INTEGER_DIV:
            return self.visit(node.left) // self.visit(node.right)
        elif node.op.type == TokenType.FLOAT_DIV:
            return float(self.visit(node.left)) / float(self.visit(node.right))

    def visit_Num(self, node):
        return node.value

    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == TokenType.PLUS:
            return +self.visit(node.expr)
        elif op == TokenType.MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node):
        var_name = node.left.value
        var_value = self.visit(node.right)

        AR = self.call_stack.peek()
        AR[var_name] = var_value

    def visit_Var(self, node):
        var_name = node.value

        AR = self.call_stack.peek()
        var_value = AR[var_name]

        return var_value

    def visit_NoOp(self, node):
        pass

    def visit_ProcedureDecl(self, node):
        pass

    def visit_ProcedureCall(self, node):
        proc_name = node.proc_name

        AR = ActivationRecord(
            name=proc_name,
            scope_name=proc_name,
            type=ARType.PROCEDURE,
            nesting_level=self.call_stack.peek().nesting_level + 1,
            execution_order=self.global_execution_order,
            outer_scope=self.call_stack.peek(),
        )

        proc_symbol = node.proc_symbol

        formal_params = proc_symbol.formal_params
        actual_params = node.actual_params

        for param_symbol, argument_node in zip(formal_params, actual_params):
            AR[param_symbol.name] = self.visit(argument_node)

        self.call_stack.push(AR)
        self.global_execution_order += 1

        if self.call_stack.size > self.MAX_RECURSION_DEPTH:
            self.error(
                error_code=ErrorCode.MAX_RECURSION_DEPTH_REACHED,
                token=node.token,
            )

        self.visit(proc_symbol.block_ast)

        self.ar_tree.push(self.call_stack.pop())

    def interpret(self):
        tree = self.semantic_analyzer.analyze()

        if tree is None:
            return ''

        self.ar_tree.build_tree(self.semantic_analyzer.scopes)

        return self.visit(tree)
