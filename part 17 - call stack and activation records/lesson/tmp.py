from Interpreter import Interpreter

if __name__ == '__main__':
    text = """program Main;
var x, y : integer;

procedure Alpha(a : integer);
    procedure Beta(b : integer);
        begin
        end;
begin
end;

procedure Alpha2(a : integer);
begin
end;

begin { Main }
   y := 7;
   x := (y + 3) * 3;
end.  { Main }
"""

    interpreter = Interpreter(text)
    interpreter.interpret()

    # for scope in interpreter.semantic_analyzer.scopes:
    #    print(scope.scope_name, scope.scope_level, scope.enclosing_scope.scope_name if scope.enclosing_scope else None)

    # print(ar_tree)
    # print(ar_tree._bf_traverse(ar_tree.root))

    # for node in ar_tree._preorder_traverse(ar_tree.root):
    #     print(node.scope.scope_name, node.scope.scope_level, '<- ' + node.scope.enclosing_scope.scope_name if node.scope.enclosing_scope else None)

    # for node in ar_tree._bf_traverse(ar_tree.root):
    #     print(node.scope.scope_name, node.scope.scope_level, '<- ' + node.scope.enclosing_scope.scope_name if node.scope.enclosing_scope else None)

    tmp = []

    for node in interpreter.ar_tree.bf_traverse(interpreter.ar_tree.root):
        tmp.append(
            [
                node.scope.scope_name,
                node.scope.scope_level,
                node.scope.enclosing_scope.scope_name if node.scope.enclosing_scope else None,
                [record for record in node.ar_records],
            ],
        )

    for t in tmp:
        print(t[0], t[1], t[2])
        for record in t[3]:
            print(record)
