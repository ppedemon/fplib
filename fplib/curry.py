from inspect import (isbuiltin, isfunction)

class Curried:
    def __init__(self, f):
        self._f = f

    def __call__(self, *args):
        val = self._f
        for arg in args:
            try:
                val = val(arg)
            except TypeError:
                raise TypeError('Too many arguments to curried function')
        """
        Bug fix: blindly currifying a callable spells trouble. For example,
        if a curried function returns a Reader instance (which is callable)
        that reader will be turned into a Curried object. Any invokation to
        a method other than __call__ will fail.

        Solution: only currify results if they're actual functions.
        Unfortunately detecting functions isn't really trivial.
        """
        #return Curried(val) if callable(val) else val
        return Curried(val) if isfunction(val) or isbuiltin(val) else val


def curry(f):
    def _curry(args, n):
        if n == 0:
            return f(*args)
        else:
            return lambda x: _curry(args + [x], n - 1)
    return Curried(_curry([], f.__code__.co_argcount))
