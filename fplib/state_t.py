from fplib.curry import curry
from fplib.monad import Monad
from fplib.transformer import Transformer


@curry
def _unpack(f, tup):
    return f(*tup)


class StateT(Monad, Transformer):
    def __init__(self, mf):
        super(StateT, self).__init__(mf)

    def fmap(self, f):
        return self.cls(lambda s: _unpack(lambda x, s0: (f(x), s0)) >> self(s))

    def apply(self, functorVal):
        return self.cls(lambda s: self(s) >> _unpack(
            lambda f, s0: functorVal(s0) >> _unpack(
            lambda x, s1: self.innermonad.unit((f(x), s1)))))

    def _bind(self, f):
        return self.cls(lambda s: self(s) >> _unpack(lambda x, s0: f(x)(s0)))

    def __call__(self, s):
        return self.unwrap(s)

    @classmethod
    def unit(cls, x):
        return cls(lambda s: cls.innermonad.unit((x, s)))

    @classmethod
    def lift(cls, m):
        return cls(lambda s: m >> (lambda x: cls.innermonad.unit((x, s))))


if __name__ == '__main__':
    from fplib.maybe import Maybe
    from fplib.transformer import trans
    T = trans(StateT, Maybe, 'StateT[Maybe]')
    print(((lambda x: x + 1) >> T.unit(1))(0))
    print((T.unit(lambda x: x + 1) & T.unit(1))(0))
    print((T.unit(1) >> (lambda x: T.unit(x+1)))(0))
    print((T.lift(Maybe.unit(1)) >> (lambda x: T.unit(x+1)))(0))
