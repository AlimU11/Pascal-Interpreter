# Part 9 - Lesson

## Grammar

```ebnf
<program> ::= <compound_statement> <DOT>

<compound_statement> ::= <BEGIN> <statement_list> <END>

<statement_list> ::= <statement> { <SEMI> <statement_list> }*

<statement> ::= <compound_statement>
              | <assignment_statement>
              | <empty>

<assignment_statement> ::= <variable> <ASSIGN> <expression>

<empty> ::= ''

<expression> ::= <term> { (<PLUS> | <MINUS>) <term> }*

<term> ::= <factor> { (<MUL> | <DIV>) <factor> }*

<factor> ::= <PLUS> <factor>
           | <MINUS> <factor>
           | <INTEGER>
           | <LPAREN> <expression> <RPAREN>
           | <variable>

<variable> ::= <ID>

<ID> ::= [a-zA-Z][a-zA-Z0-9]*

<INTEGER> ::= <digit>+

<digit> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

<BEGIN> ::= 'BEGIN'
<END> ::= 'END'
<DOT> ::= '.'
<SEMI> ::= ';'
<ASSIGN> ::= ':='
<PLUS> ::= '+'
<MINUS> ::= '-'
<MUL> ::= '*'
<DIV> ::= '/'
<LPAREN> ::= '('
<RPAREN> ::= ')'
```

## Diagram

### Program

![](src/diagram1.svg)

### Compound Statement

![](src/diagram2.svg)

### Statement List

![](src/diagram3.svg)

### Statement

![](src/diagram4.svg)

### Assignment Statement

![](src/diagram5.svg)

### Variable

![](src/diagram6.svg)

### Empty Statement

![](src/diagram7.svg)

### Factor

![](src/diagram8.svg)

## Reference

https://ruslanspivak.com/lsbasi-part9/
