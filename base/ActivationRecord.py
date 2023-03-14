class ActivationRecord:
    def __init__(self, name, scope_name, type, nesting_level, execution_order, outer_scope):
        self.name = name
        self.scope_name = scope_name
        self.type = type
        self.nesting_level = nesting_level
        self.execution_order = execution_order
        self.members = {}
        self.outer_scope = outer_scope

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        val = self.members.get(key)

        if not val:
            val = self.outer_scope[key]

        return val

    def __str__(self):
        lines = [
            '{level}: {type} {name} (execution order: {execution_order})'.format(
                level=self.nesting_level,
                type=self.type.name,
                name=self.name,
                execution_order=self.execution_order,
            ),
        ]
        for name, val in self.members.items():
            lines.append(f'   {name:<20}: {val}')

        s = '\n'.join(lines)
        return s

    def __repr__(self):
        return self.__str__()
