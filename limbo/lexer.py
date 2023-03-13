from typing import Optional
from re import match
from parser import Parse, Parser, Success, Failure


class Match(Parser):
    """
    Match(Parser)

    Consumes a parse string if it matches a given token.
    """

    def __init__(self, token: str):
        self.token = token


    def __call__(self, parse: Parser) -> Parse:

        lexeme = match(self.token, parse.string)

        if lexeme == None:
            return Failure()(parse)

        return Success()(Parse(
                string = parse.string[lexeme.end() :],
                result = lexeme.group(),
        ))
