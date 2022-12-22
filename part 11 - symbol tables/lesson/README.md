# Part 11 - Lesson

## Grammar

```ebnf
# Program

<program> ::= <PROGRAM> <variable> <SEMI> <block> <DOT>

# Block

<block> ::= <declarations> <compound_statement>

# Declaration

<declarations> ::= [ <VAR> { <variable_declaration> <SEMI> }+ ]

<variable_declaration> ::= <ID> { <COMMA> <ID> }* <COLON> <type_spec>

<type_spec> ::= <INTEGER_TYPE> | <REAL_TYPE>

# Statement

<compound_statement> ::= <BEGIN> <statement_list> <END>

<statement_list> ::= <statement> { <SEMI> <statement_list> }*

<statement> ::= <compound_statement>
              | <assignment_statement>
              | <empty>

<assignment_statement> ::= <variable> <ASSIGN> <expression>

<empty> ::= ''

# Mathemathical Expression

<expression> ::= <term> { (<PLUS> | <MINUS>) <term> }*

<term> ::= <factor> { (<MUL> | <INTEGER_DIV> | <FLOAT_DIV>) <factor> }*

<factor> ::= <PLUS> <factor>
           | <MINUS> <factor>
           | <INTEGER>
           | <REAL>
           | <LPAREN> <expression> <RPAREN>
           | <variable>

# Variables

<variable> ::= <ID>

<ID> ::= [a-zA-Z_][a-zA-Z0-9_]*

# Numerical Values

<INTEGER> ::= <digit>+
<REAL> ::= <digit>+ [ <DOT> <digit>+ ]

<digit> ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

# Reserved words

<PROGRAM> ::= 'PROGRAM'
<BEGIN> ::= 'BEGIN'
<END> ::= 'END'
<VAR> ::= 'VAR'
<INTEGER_TYPE> ::= 'INTEGER'
<REAL_TYPE> ::= 'REAL'

# Symbols

<DOT> ::= '.'
<SEMI> ::= ';'
<COMMA> ::= ','
<COLON> ::= ':'
<LPAREN> ::= '('
<RPAREN> ::= ')'

# Operators

<ASSIGN> ::= ':='
<PLUS> ::= '+'
<MINUS> ::= '-'
<MUL> ::= '*'
<FLOAT_DIV> ::= '/'
<INTEGER_DIV> ::= 'DIV'
```

## Diagram

### Program

![](src/diagram1.svg)

### Block

![](src/diagram2.svg)

### Declarations

![](src/diagram3.svg)

### Variable Declaration

![](src/diagram4.svg)

### Type Specification

![](src/diagram5.svg)

### Compound Statement

![](src/diagram6.svg)

### Statement List

![](src/diagram7.svg)

### Statement

![](src/diagram8.svg)

### Assignment Statement

![](src/diagram9.svg)

### Empty Statement

![](src/diagram10.svg)

### Expression

![](src/diagram11.svg)

### Term

![](src/diagram12.svg)

### Factor

![](src/diagram13.svg)

### Variable

![](src/diagram14.svg)

## Reference

https://ruslanspivak.com/lsbasi-part11/
