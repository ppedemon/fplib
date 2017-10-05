from fplib.monad import Monad

class State(Monad):
    def __init__(self, f):
        self._f = f

    def __call__(self, s):
        return self._f(s)

    def fmap(self, f):
        @State
        def step(s):
            x, s0 = self(s)
            return f(x), s0
        return step

    def apply(self, functorVal):
        @State
        def step(s):
            f, s0 = self(s)
            x, s1 = functorVal(s0)
            return f(x), s1
        return step

    def _bind(self, f):
        @State
        def step(s):
            x, s0 = self(s)
            return f(x)(s0)
        return step

    @classmethod
    def unit(cls, x):
        return State(lambda s: (x, s))


if __name__ == '__main__':
    from fplib.curry import curry
    from fplib.functor import unit

    @curry
    def add(x, y):
        return x + y

    f = unit(State, add)
    x = unit(State, 1)
    y = unit(State, 2)
    print((f & x & y)(()))

    print((y >> (lambda x: unit(State, x+10)))(()))
