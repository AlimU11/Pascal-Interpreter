from Symbol import BuiltinTypeSymbol


class ScopedSymbolTable(object):
    def __init__(self, scope_name, scope_level, enclosing_scope=None):
        self._symbols = {}
        self.scope_name = scope_name
        self.scope_level = scope_level
        self.enclosing_scope = enclosing_scope
        print('Scope: %s Level: %s' % (self.scope_name, self.scope_level))

    def _init_builtins(self):
        self.define(BuiltinTypeSymbol('INTEGER'))
        self.define(BuiltinTypeSymbol('REAL'))

    def __str__(self):
        return [self.scope_name, self.scope_level, self.enclosing_scope, [value for value in self._symbols.values()]]

    def __repr__(self):
        return self.__str__()

    def define(self, symbol):
        print('Define: %s' % symbol)
        self._symbols[symbol.name] = symbol

    def lookup(self, name, current_scope_only=False):
        print('Lookup: %s at %s' % (name, self.scope_name))

        symbol = self._symbols.get(name)

        if symbol is not None:
            return symbol

        if current_scope_only:
            return None

        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup(name)

    def insert(self, symbol):
        print('Insert: %s' % symbol)
        self._symbols[symbol.name] = symbol
