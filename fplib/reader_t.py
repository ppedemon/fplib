from fplib.misc import (const, compose)
from fplib.monad import Monad
from fplib.transformer import Transformer


class ReaderT(Monad, Transformer):
    def __init__(self, fm):
        super(ReaderT, self).__init__(fm)

    def fmap(self, f):
        return self.cls(compose(lambda x: f >> x, self.unwrap))

    def apply(self, functorVal):
        return self.cls(lambda r: self(r) & functorVal(r))

    def _bind(self, f):
        return self.cls(lambda r: self(r) >> (lambda x: f(x)(r)))

    def __call__(self, r):
        return self.unwrap(r)

    @classmethod
    def unit(cls, x):
        return cls(const(cls.innermonad.unit(x)))

    @classmethod
    def lift(cls, m):
        return cls(const(m))


if __name__ == '__main__':
    from fplib.maybe import (Just, Maybe)
    from fplib.transformer import trans
    T = trans(ReaderT, Maybe, 'ReaderT[Maybe]')
    print(((lambda x: x + 1) >> T.unit(1))(0))
    print((T.unit(lambda x: x + 1) & T.unit(1))(0))
    print((T.unit(1) >> (lambda x: T.unit(x+1)))(0))
    print((T.lift(Just(1)) >> (lambda x: T.unit(x+1)))(0))
