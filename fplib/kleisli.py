from fplib.curry import curry
from fplib.list import List


@curry
def mapm(f, xs, M=None):
    if len(xs) == 0:
        if not M:
            raise TypeError('unresolved monad type')
        return M.unit(List())
    m = f(xs[0])
    M = M or m.__class__
    return m >> (
        lambda y: mapm(f, xs[1:], M) >> (
        lambda ys: M.unit(List(y) + ys)))
