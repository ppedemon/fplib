from fplib.misc import compose
from fplib.monad import Monad
from fplib.transformer import Transformer

class IdT(Monad, Transformer):
    def __init__(self, m):
        super(IdT, self).__init__(m)

    def fmap(self, f):
        return self.cls(f >> self.unwrap)

    def apply(self, functorVal):
        return self.cls(self.unwrap & functorVal.unwrap)

    def _bind(self, f):
        return self.cls(self.unwrap >> (lambda x: f(x).unwrap))

    @classmethod
    def unit(cls, x):
        return cls(cls.innermonad.unit(x))

    @classmethod
    def lift(cls, m):
        return cls(m)


if __name__ == '__main__':
    from fplib.maybe import Maybe
    from fplib.misc import compose
    from fplib.transformer import (trans, transchain, translift)
    #T = trans(IdT, Maybe, 'IdT[Maybe]')
    T = transchain((IdT,'OuterIdT[Maybe]'), (IdT,'InnerIdT[Maybe]'), Maybe)
    print(T.unit(20) >> (lambda x: T.unit(x + 1)))
    print(translift(T, Maybe.unit(20)) >> (lambda x: T.unit(x + 1)))
    print(compose(lambda x: x + 1, len) >> T.unit('a'))
    print((lambda x: x + 1) >> (len >> T.unit('a')))
    print(len >> T.unit('a'))
