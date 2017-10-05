from fplib.curry import curry
from fplib.functor import Functor


class Applicative(Functor):
    def __and__(self, functorVal):
        return self.apply(functorVal)

    def apply(self, functorVal):
        raise NotImplementedError('apply not defined')

    def left(self, other):
        return lift2(lambda x, _: x)(self, other)

    def right(self, other):
        return lift2(lambda _, x: x)(self, other)


@curry
def lift2(f, a, b):
    return curry(f) >> a & b
