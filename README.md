# Pascal Interpreter

A simple Pascal interpreter based on [Let's Build a Simple Interpreter](https://github.com/rspivak/lsbasi) series by [Ruslan Spivak](https://github.com/rspivak/) with usage of [EBNF grammar tester](https://mdkrajnak.github.io/ebnftest/) by [mdkrajnak](https://github.com/mdkrajnak/), [TatSu](https://github.com/neogeny/TatSu) and [railroad diagrams](https://github.com/tabatkins/railroad-diagrams).

## Project structure

- `.github/workflows` - workflows for running tests
- `base` - files for building the interpreter at its current state
- `part [1-9][0-9]*( - [a-zA-Z ]*)?` - part that reflects the state of the interpreter at the end of the corresponding part of the series
- `src` - images for this README
- `test` - test modules and test files for the interpreter in each part

## Current state

![img.png](src/img.png)

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

<factor> ::= <PLUS> <factor>
           | <MINUS> <factor>
           | <INTEGER>
           | <LPAREN> <expression> <RPAREN>
           | <variable>

<expression> ::= <term> { (<PLUS> | <MINUS>) <term> }*

<term> ::= <factor> { (<MUL> | <DIV>) <factor> }*

<variable> ::= <ID>

<ID> ::= [a-zA-Z_][a-zA-Z0-9_]*

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
<DIV> ::= 'DIV'
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

### Expression

![](src/diagram9.svg)

### Term

![](src/diagram10.svg)
