from dataclasses import dataclass


last = lambda x: x[-1]
init = lambda x: x[: -1]


@dataclass
class parser:
        f: callable = None
        __call__ = lambda self, x: self.f(x)
        __or__ = lambda f, g: parser(lambda x: f(x) or g(x))
        __add__ = lambda f, g: parser(lambda x: (x := p(x)) and (y := q(x)) and (init(x) + y))
        __neg__= lambda f: parser(lambda x: (y := f(x)) and (*init(x), last(y)))
        __gt__ = lambda f, g: parser(lambda x: (x := f(x)) and (g(*init(x)), last(x)))


import re

def match(token):

        def f(x):
                string = last(x)
                lexeme = re.match(token, string)

                if lexeme:
                        return lexeme.group(), string[lexeme.end() :]
        return parser(f)
