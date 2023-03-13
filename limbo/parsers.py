"""
Common parsers.
"""

from dataclasses import dataclass
from re import match
from combinators import *


@dataclass
class Token(Parser):
    token: str

    def __call__(self, parse: Parser) -> Parse:

        lexeme = match(self.token, parse[0])

        if lexeme:
                return (parse[0][lexeme.end() :], lexeme.group())

    __repr__ = lambda self: f"\"{self.token}\""
