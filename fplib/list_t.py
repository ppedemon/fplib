from fplib.curry import curry
from fplib.kleisli import mapm
from fplib.list import (List, concat)
from fplib.monad import Monad
from fplib.transformer import Transformer

class ListT(Monad, Transformer):
    def __init__(self, m):
        super(ListT, self).__init__(m)

    def fmap(self, f):
        return self.cls((lambda xs: f >> xs) >> self.unwrap)

    def apply(self, functorVal):
        return self.cls(curry(lambda fs, xs: fs & xs) >>
            self.unwrap & functorVal.unwrap)

    def _bind(self, f):
        return self.cls(self.unwrap >> (
            lambda xs: mapm(lambda x: f(x).unwrap, xs, self.innermonad) >> (
            lambda xss: self.innermonad.unit(concat(*xss)))))

    @classmethod
    def unit(cls, x):
        return cls(cls.innermonad.unit(List(x)))

    @classmethod
    def lift(cls, m):
        return cls(List >> m)


if __name__ == '__main__':
    from fplib.maybe import (Maybe, Just)
    from fplib.transformer import trans
    T = trans(ListT, Maybe, 'ListT[Maybe]')
    print((lambda x: x + 1) >> T.unit(1))
    print(T.unit('a') >> (lambda x: T.unit(x + '!')))
    print(T.unit(lambda x: len(x + '!')) & T.lift(Just('a')))
