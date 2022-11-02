# Part 7 - Lesson

## Grammar

```ebnf
<expression> ::= <term> { ("+" | "-") <term> }*
<term>       ::= <factor> { ("*" | "/") <factor> }*
<factor>     ::= <INTEGER> | "(" <expression> ")"
<INTEGER>    ::= <digit>+
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

## Diagram

### Expr

![](diagram1.svg)

### Term

![](diagram2.svg)

### Factor

![](diagram3.svg)

## Reference

https://ruslanspivak.com/lsbasi-part7/
