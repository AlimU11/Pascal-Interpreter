class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + str(type(node).__name__).lower()
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')
