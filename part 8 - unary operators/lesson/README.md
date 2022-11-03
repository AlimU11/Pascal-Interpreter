# Part 8 - Lesson

## Grammar

```ebnf
<expression> ::= <term> { (<plus> | <minus>) <term> }*
<term>       ::= <factor> { (<mul> | <div>) <factor> }*
<factor>     ::= (<plus> | <minus>) <factor> | <integer> | <lparen> <expression> <rparen>
<integer>    ::= <digit>+
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<plus>       ::= "+"
<minus>      ::= "-"
<mul>        ::= "*"
<div>        ::= "/"
<lparen>     ::= "("
<rparen>     ::= ")"
```

## Diagram

### Expr

![](diagram1.svg)

### Term

![](diagram2.svg)

### Factor

![](diagram3.svg)

## Reference

https://ruslanspivak.com/lsbasi-part8/
