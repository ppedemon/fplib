from fplib.curry import (Curried, curry)
from fplib.monad import Monad
from fplib.misc import (const, compose)

class Reader(Curried, Monad):
    def __init__(self, f):
        super().__init__(f)

    def fmap(self, f):
        return Reader(compose(f, self))

    def apply(self, functorVal):
        return Reader(lambda s: self(s)(functorVal(s)))

    def _bind(self, f):
        return Reader(lambda s: f(self(s))(s))

    @classmethod
    def unit(cls, x):
        return Reader(const(x))


@curry
def lookup(k, d):
    return d[k]

@curry
def add(x, y):
    return x + y

def neg(x):
    return -x

if __name__ == '__main__':
    from fplib.functor import unit
    f = Reader(const(add))
    k = Reader(const(1))
    a = Reader(lookup('a'))
    b = Reader(lookup('b'))
    n = Reader(const(neg))
    print((f & (n & b) & a)(dict(a=1, b=2)))
    print((b >> (lambda x: unit(Reader, x + 1)))(dict(a=1, b=2)))
