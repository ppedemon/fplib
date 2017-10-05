from fplib.misc import (compose, const, ident, fail)
from fplib.monad import Monad
from fplib.monoid import Monoid

class Maybe(Monad, Monoid):
    @classmethod
    def unit(cls, x):
        return Just(x)

    @classmethod
    def zero(cls):
        return Nothing

    def cata(self, f, g):
        return f(self.value) if isinstance(self, Just) else g()

    def get(self):
        return self.cata(ident, lambda: fail('Maybe.get: Nothing'))

    def fmap(self, f):
        return self.cata(compose(Just, f), lambda: self)

    def apply(self, functorVal):
        return self.cata(lambda f: f >> functorVal, lambda: self)

    def _bind(self, f):
        return self.cata(f, lambda: self)

    def plus(self, x):
        return self.cata(
            lambda p: x.cata(lambda q: Just(p + q), lambda: self),
            lambda: x)

    def __str__(self):
        return self.cata(lambda x: f'Just({x})', lambda: 'Nothing')

    def __neq__(self, other):
        return not self == other

    def __or__(self, other):
        return self.getOrElse(other)

    def getOrElse(self, other):
        return self.cata(ident, lambda: other)

    def isJust(self):
        return self.cata(const(True), lambda: False)

    def isEmpty(self):
        return not self.isJust()

    def orElse(self, other):
        return self.cata(const(self), lambda: other)

    def forall(self, pred):
        return self.cata(pred, lambda: True)

    def exists(self, pred):
        return self.cata(pred, lambda: False)

    def filter(self, pred):
        return self >> (lambda x: self if pred(x) else Nothing)


class _Nothing(Maybe):
    def __eq__(self, other):
        return isinstance(other, _Nothing)

Nothing = _Nothing()


class Just(Maybe):
    def __init__(self, x):
        self._value = x

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        return isinstance(other, Just) and other.value == self.value

if __name__ == '__main__':
    print(Nothing|20)
    print(Just(1)|0)
    print(Just(23).isJust())
    print(Nothing.isJust())
    print(Just(23).isEmpty())
    print(Nothing.isEmpty())
    print(Just(23).orElse(Just(-1)))
    print(Nothing.orElse(Just(-1)))

    print(Just(1).forall(lambda x: x > 0))
    print(Nothing.forall(lambda x: x > 0))
    print(Just(0).forall(lambda x: x > 0))
    print(Nothing.forall(lambda x: x > 0))

    print(Just(1).exists(lambda x: x > 0))
    print(Nothing.exists(lambda x: x > 0))
    print(Just(0).exists(lambda x: x > 0))
    print(Nothing.exists(lambda x: x > 0))

    print(Just(1).filter(lambda x: x > 0))
    print(Nothing.filter(lambda x: x > 0))
    print(Just(0).filter(lambda x: x > 0))
    print(Nothing.filter(lambda x: x > 0))
