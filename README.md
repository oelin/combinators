# Combinators

Parser combinators for Python.

## Introduction

Combinators is a tiny parser combinator library which allows you to construct sophisticated parsers using context-free grammars.


```py
# A parser for propositional logic.

from combinators import Match, Foward


# Terminals.

LeftBrace = Match("\(")

RightBrace = Match("\)")

UnaryConnective = Match("¬")

BinaryConnective = Match("[v\^>]")

Literal = Match("[A-Z]")


# Nonterminals.

Expression = Forward() # Forward reference.

UnaryExpression = UnaryConnective + Expression

BinaryExpression = LeftBrace + Expression + BinaryConnective + Expression + RightBrace

Expression.is(Literal | UnaryExpression | BinaryExpression)
```
