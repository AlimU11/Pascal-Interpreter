import json

from Symbol import BuiltinTypeSymbol


class ScopedSymbolTable(object):
    def __init__(self, scope_name, scope_level, enclosing_scope=None):
        self._symbols = {}
        self.scope_name = scope_name
        self.scope_level = scope_level
        self.enclosing_scope = enclosing_scope

    def _init_builtins(self):
        self.insert(BuiltinTypeSymbol('INTEGER'))
        self.insert(BuiltinTypeSymbol('REAL'))

    def __str__(self):
        return json.dumps(
            {
                'scope_name': self.scope_name,
                'scope_level': self.scope_level,
                'enclosing_scope': self.enclosing_scope.scope_name if self.enclosing_scope else None,
                'symbols': [str(symbol) for symbol in self._symbols.values()],
            },
        )

    def __repr__(self):
        return self.__str__()

    def insert(self, symbol):
        self._symbols[symbol.name] = symbol
        symbol.scope = self

    def lookup(self, name, current_scope_only=False):
        symbol = self._symbols.get(name)

        if symbol is not None:
            return symbol

        if current_scope_only:
            return None

        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup(name)

    def lookup_scope_level(self, name):
        symbol = self._symbols.get(name)

        if symbol is not None:
            return self.scope_level

        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup_scope_level(name)
