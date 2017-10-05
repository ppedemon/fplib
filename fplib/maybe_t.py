from fplib.misc import ident
from fplib.maybe import (Just, Nothing)
from fplib.monad import Monad
from fplib.transformer import Transformer

class MaybeT(Monad, Transformer):
    def __init__(self, m):
        super(MaybeT, self).__init__(m)

    def fmap(self, f):
        return self.cls((lambda mb: f >> mb) >> self.unwrap)

    def apply(self, functorVal):
        return self.cls(self.unwrap >> (lambda mf: mf.cata(
            lambda f: (functorVal.unwrap >> (lambda mv: mv.cata(
                lambda v: self.innermonad.unit(Just(f(v))),
                lambda: self.innermonad.unit(Nothing)))),
            lambda: self.innermonad.unit(Nothing))))

    def _bind(self, f):
        return self.cls(self.unwrap >> (lambda mv: mv.cata(
            lambda v: f(v).unwrap,
            lambda: self.innermonad.unit(Nothing))))

    @classmethod
    def unit(cls, x):
        return cls(cls.innermonad.unit(Just(x)))

    @classmethod
    def lift(cls, m):
        return cls(Just >> m)


if __name__ == '__main__':
    from fplib.ident_t import IdT
    from fplib.list import List
    from fplib.transformer import (trans, transchain, translift)
    T = transchain((MaybeT, 'MaybeT'), (IdT, 'IdT'), List)
    print(len >> T.unit('a'))
    print(T.unit('abc') >> (lambda x: T.unit(len(x))))
    print(T.unit(len) & T.unit('abc'))
    print(translift(T, List(len, lambda x: x + '!')) & translift(T, List('abc', 'abcd')))
