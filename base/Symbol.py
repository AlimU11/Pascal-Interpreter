class Symbol(object):
    def __init__(self, name, type=None):
        self.name = name
        self.type = type

    def __str__(self):
        return "<{class_name}(name='{name}'{type})>".format(
            class_name=self.__class__.__name__,
            name=self.name,
            type=', type=' + self.type if self.type else '',
        )


class VarSymbol(Symbol):
    def __init__(self, name, type):
        super().__init__(name, type)

    def __str__(self):
        return "<{class_name}(name='{name}', type='{type}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
            type=self.type,
        )

    def __repr__(self):
        return self.__str__()


class BuiltinTypeSymbol(Symbol):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<{class_name}('{name}')>".format(
            class_name=self.__class__.__name__,
            name=self.name,
        )


class ProcedureSymbol(Symbol):
    def __init__(self, name, formal_params=None):
        super(ProcedureSymbol, self).__init__(name)
        self.formal_params = formal_params if formal_params else []
        self.block_ast = None

    def __str__(self):
        return '<{class_name}(name={name}, parameters={params})>'.format(
            class_name=self.__class__.__name__,
            name=self.name,
            params=self.formal_params,
        )

    def __repr__(self):
        return self.__str__()


class BuiltInProcedureSymbol(ProcedureSymbol):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return '<{class_name}(name={name}, parameters={params})>'.format(
            class_name=self.__class__.__name__,
            name=self.name,
            params=self.formal_params,
        )

    def __repr__(self):
        return self.__str__()
