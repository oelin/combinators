# Combinators

Parser combinators for Python.

## Introduction

Combinators is a tiny parser combinator library which allows you to construct sophisticated parsers using context-free grammars.


```py
# A parser for propositional logic.

from combinators import Match, Lambda


# Terminals.

LeftBrace = Match("\(")

RightBrace = Match("\)")

UnaryConnective = Match("¬")

BinaryConnective = Match("[v\^>]")

Literal = Match("[A-Z]")


# Nonterminals.

Expression = Lambda(lambda p: Expression(p)) # Lazy evaluation.

UnaryExpression = UnaryConnective & Expression

BianryExpression = LeftBrace & Expression & BinaryConnective & Expression & RightBrace

Expression = Literal | UnaryExpression | BinaryExpression
```
