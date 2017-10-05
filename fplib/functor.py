class Functor:
    def __rrshift__(self, f):
        return self.fmap(f)

    @classmethod
    def unit(cls, x):
        raise NotImplementedError('unit not defined')

    def fmap(self, f):
        raise NotImplementedError('fmap not defined')


def unit(cls, x):
    return cls.unit(x)
