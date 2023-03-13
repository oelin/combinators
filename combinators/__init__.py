from . combinators import Parse, Parser, And, Or, Maybe, Lambda
from . parsers import Match


# Operators.

Parser.__and__ = And
Parser.__or__ = Or
