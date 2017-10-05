from uuid import uuid4
from functools import reduce


class Transformer:
    innermonad = None

    def __init__(self, m):
        self._m = m
        self._cls = self.__class__

    @property
    def unwrap(self):
        return self._m

    @property
    def cls(self):
        return self._cls

    def __str__(self):
        return f'{self.cls.__name__}({self.unwrap})'

    @classmethod
    def lift(cls, m):
        raise NotImplementedError('lift not defined')


def trans(tcls, innermonad, name=None):
    name = name or f'{tcls.__name__}_{uuid4()}'.replace('-','_')
    return type(name, (tcls,), {'innermonad': innermonad, 'ownclass':tcls})

def transchain(*classes):
    innermonad = classes[-1]
    def _trans(m, t):
        return trans(t[0], m, t[1]) if type(t) == tuple else trans(t, m)
    return reduce(_trans, reversed(classes[:-1]), innermonad)

def translift(tcls, m):
    if issubclass(tcls.innermonad, Transformer):
        return tcls.lift(translift(tcls.innermonad, m))
    else:
        return tcls.lift(m)
