from itertools import chain
from fplib.monad import Monad
from fplib.monoid import Monoid

class List(list, Monad, Monoid):
    def __init__(self, *args):
        super().__init__(args)

    @classmethod
    def unit(cls, x):
        return List(x)

    @classmethod
    def zero(cls):
        return List()

    def fmap(self, f):
        return List(*map(f, self))

    def apply(self, functorVal):
        return List(*[f(x) for f in self for x in functorVal])

    def _bind(self, f):
        return concat(*map(f, self))

    def plus(self, xs):
        return concat(self, xs)

    def __add__(self, xs):
        return self.plus(xs)

    def __getitem__(self, key):
        result = super().__getitem__(key)
        return List(*result) if isinstance(key, slice) else result

    def __str__(self):
        return 'List({})'.format(','.join(str(x) for x in self))


def concat(*lists):
    return List(*list(chain(*lists)))

if __name__ == '__main__':
    print(concat(List(1,2,3), List(4,5,6)))
