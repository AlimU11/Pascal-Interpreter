from base.ActivationRecord import ActivationRecord
from base.ARNode import ARNode


class ARTree:
    def __init__(self):
        self.root: ARNode
        self._size: int = 0

    def build_tree(self, scopes):
        """
        Builds the tree from the list of scopes. The first scope in the list is
        built-in scope and the root of the tree. Its only child is second scope in the list
        - the global scope. Other scopes are children or ancestors of the global scope. It
        is guaranteed that that each scope is unique and that at least built-in and global
        scopes are present in the list.
        """
        self.root = ARNode(scopes[0])
        self._size = 1

        for scope in scopes[1:]:
            node = ARNode(scope)
            parent = self._find_parent(scope, self.root)
            parent.children.append(node)
            self._size += 1

    def _find_parent(self, scope, root: ARNode) -> ARNode:
        """
        Finds the parent of the given scope. It is guaranteed that the scope has a parent.
        """

        if scope.enclosing_scope == root.scope and scope.scope_level == root.scope.scope_level + 1:
            return root
        else:
            for child in root.children:
                node = self._find_parent(scope, child)
                if node:
                    return node

        return ARNode(None)

    def _find_node(self, name: str, level: int, root: ARNode) -> ARNode:
        """
        Finds the node with the given name and level. It is guaranteed that the node exists.
        """
        if root.scope.scope_name == name and root.scope.scope_level == level:
            return root
        else:
            for child in root.children:
                node = self._find_node(name, level, child)
                if node:
                    return node

        return ARNode(None)

    def find(self, name: str, level: int) -> list[ActivationRecord]:
        """
        Finds the activation record with the given name and level. It is guaranteed that the
        record exists.
        """
        node = self._find_node(name, level, self.root)
        return node.ar_records

    def push(self, AR: ActivationRecord) -> None:
        node = self._find_node(AR.scope_name, AR.nesting_level, self.root)
        node.ar_records.append(AR)

    def __str__(self):
        return '\n'.join([i.__str__() for i in self._bf_traverse(self.root)])

    def preorder_traverse(self, root: ARNode) -> list[ARNode]:
        """
        Performs a pre-order traversal of the tree.
        Returns a list of nodes in the order they were visited.
        """
        nodes = [root]

        for child in root.children:
            nodes += self.preorder_traverse(child)

        return nodes

    def bf_traverse(self) -> list[ARNode]:
        return self._bf_traverse(self.root)

    def _bf_traverse(self, root: ARNode) -> list[ARNode]:
        """
        Performs a breadth-first traversal of the tree.
        Returns a list of nodes in the order they were visited.
        """
        nodes = [root]
        queue = [root]

        while queue:
            node = queue.pop(0)
            for child in node.children:
                nodes.append(child)
                queue.append(child)

        return nodes

    def __len__(self) -> int:
        return self._size

    @property
    def size(self) -> int:
        return self._size
