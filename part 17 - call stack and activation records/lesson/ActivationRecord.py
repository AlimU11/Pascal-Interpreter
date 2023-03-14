class ActivationRecord:
    def __init__(self, name, scope_name, type, nesting_level, execution_order):
        self.name = name
        self.scope_name = scope_name
        self.type = type
        self.nesting_level = nesting_level
        self.exdecution_order = execution_order
        self.members = {}

    def __setitem__(self, key, value):
        self.members[key] = value

    def __getitem__(self, key):
        return self.members[key]

    def get(self, key):
        return self.members.get(key)

    def __str__(self):
        lines = [
            '{level}: {type} {name} (execution order: {execution_order})'.format(
                level=self.nesting_level,
                type=self.type.name,
                name=self.name,
                execution_order=self.exdecution_order,
            ),
        ]
        for name, val in self.members.items():
            lines.append(f'   {name:<20}: {val}')

        s = '\n'.join(lines)
        return s

    def __repr__(self):
        return self.__str__()
