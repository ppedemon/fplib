from fplib.applicative import Applicative

class Monad(Applicative):
    def __rshift__(self, f):
        return self.bind(f)

    def bind(self, f):
        return self._bind(f) if callable(f) else self.bind(lambda _: f)

    def _bind(self, f):
        raise NotImplementedError('_bind not defined')
