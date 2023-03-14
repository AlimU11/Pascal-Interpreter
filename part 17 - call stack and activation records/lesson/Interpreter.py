from ActivationRecord import ActivationRecord
from ARTree import ARTree
from ARType import ARType
from CallStack import CallStack
from NodeVisitor import NodeVisitor
from SemanticAnalyzer import SemanticAnalyzer
from TokenType import TokenType


class Interpreter(NodeVisitor):
    def __init__(self, text):
        self.semantic_analyzer = SemanticAnalyzer(text)
        self.call_stack = CallStack()
        self.ar_tree = ARTree()
        self.global_execution_order = 0

    def visit_Program(self, node):
        program_name = node.name

        AR = ActivationRecord(
            name=program_name,
            scope_name='global',
            type=ARType.PROGRAM,
            nesting_level=1,
            execution_order=self.global_execution_order,
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
        var_value = AR.get(var_name)

        return var_value

    def visit_NoOp(self, node):
        pass

    def visit_ProcedureDecl(self, node):
        pass

    def visit_ProcedureCall(self, node):
        pass

    def interpret(self):
        tree = self.semantic_analyzer.analyze()

        if tree is None:
            return ''

        self.ar_tree.build_tree(self.semantic_analyzer.scopes)

        return self.visit(tree)
