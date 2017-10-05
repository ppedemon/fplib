from fplib.monad import Monad

class Id(Monad):
    def __init__(self, x):
        self._value = x

    @classmethod
    def unit(cls, x):
        return Id(x)

    @property
    def value(self):
        return self._value

    def fmap(self, f):
        return Id(f(self.value))

    def apply(self, functorVal):
        return self.value >> functorVal

    def _bind(self, f):
        return f(self.value)

    def __eq__(self, other):
        return isinstance(other, Id) and self.value == other.value

    def __str__(self):
        return f'Id({str(self.value)})'
