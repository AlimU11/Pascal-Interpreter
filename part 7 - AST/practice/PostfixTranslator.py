from AST import AST, BinOp, Num


class PostfixTranslator:
    def __init__(self, root: AST):
        self.root = root
        self.postfix_translation = []

    def translate(self):
        self.visit(self.root)
        return self.postfix_translation

    def visit(self, node: AST):
        if isinstance(node, BinOp):
            self.visit(node.left)
            self.visit(node.right)
            self.postfix_translation.append(node.op.value)
        elif isinstance(node, Num):
            self.postfix_translation.append(node.value)
