# Combinators

Parser combinators for Python.

## Introduction

Combinators is a tiny parser combinator library which allows you to construct sophisticated parsers using a context-free grammar.


```py
# Parser for propositional logic.

from combinators import Match, Lambda

Letter = Match("[A-Z]")

Expression = Lambda(lambda p: Expression(p)) # Placeholder.

Unary = Match("¬") & Expression

Bianry = Match("\(") & Expression & Match("[v\^>]") & Expression & Match("\)")

Expression = Literal | Unary | Binary
```
