from ActivationRecord import ActivationRecord
from ScopedSymbolTable import ScopedSymbolTable


class ARNode:
    def __init__(self, scope):
        self.scope: ScopedSymbolTable = scope
        self.ar_records: list[ActivationRecord] = []
        self.children: list[ARNode] = []

    def __str__(self):
        return f'{self.scope.scope_name} {self.scope.scope_level} <- {self.scope.enclosing_scope.scope_name if self.scope.enclosing_scope else None}'
