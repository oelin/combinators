from typing import Any, Tuple, Optional
from dataclasses import dataclass


Parse = Optional[Tuple[str, Any]]


# Parsers.

class Parser:

    def __call__(self, parse: Parse) -> Parse:
        raise NotImplementedError()


class Nothing(Parser):

    __call__ = lambda _, parse: parse
    __repr__ = lambda _: 'ɛ'


# Combinators.

def And(p: Parser, q: Parser) -> Parser:

    class AndParser(Parser):

        __call__ = lambda _, parse: (parse := p(parse)) and q(parse)
        __repr__ = lambda _: f'{p} {q}'

    return AndParser()


def Or(p: Parser, q: Parser) -> Parser:

    class OrParser(Parser):

        __call__ = lambda _, parse: p(parse) or q(parse)
        __repr__ = lambda _: f'({p} | {q})'

    return OrParser()


def Maybe(p: Parser) -> Parser:

    class MaybeParser(Parser):

        __call__ = lambda _, parse: p(parse) or parse
        __repr__ = lambda _: f'[{p}]'

    return MaybeParser()


def Lambda(p: Parser) -> Parser:

    class LambdaParser(Parser):
        __call__ = p
        __repr__ = lambda _: str(p)

    return LambdaParser()
