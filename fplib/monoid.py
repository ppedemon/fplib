import operator
from functools import reduce


class Monoid:
    def __add__(self, x):
        return self.plus(x)

    def plus(self, x):
        raise NotImplementedError('plus not defined')

    @classmethod
    def zero(cls):
        raise NotImplementedError('zero not defined')


_builtin_monoids = {
  int: 0,
  float: .0,
  str: '',
  list: []
}


def zero(cls):
    if issubclass(cls, Monoid):
        return cls.zero()
    if cls in _builtin_monoids:
        return _builtin_monoids[cls]
    raise TypeError(f'Invalid monoid type: {cls.__name__}')


def concat(*monoids):
    return reduce(operator.add, monoids)
