from AST import AST, BinOp, Num


class PrefixTranslator:
    def __init__(self, root: AST):
        self.root = root
        self.prefix_translation = []

    def translate(self):
        self.visit(self.root)
        return self.prefix_translation

    def visit(self, node: AST):
        if isinstance(node, BinOp):
            self.prefix_translation.append(node.op.value)
            self.visit(node.left)
            self.visit(node.right)
        elif isinstance(node, Num):
            self.prefix_translation.append(node.value)
