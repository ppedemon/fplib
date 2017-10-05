import itertools
import operator
import random
import string

from fplib.ident import Id
from fplib.list import List
from fplib.maybe import (Just, Nothing)
from fplib.reader import Reader
from fplib.state import State


def repeatfunc(func, times=None, *args):
    if times is None:
        return itertools.starmap(func, itertools.repeat(args))
    return itertools.starmap(func, itertools.repeat(args, times))


def random_ints(lo, hi):
    return repeatfunc(random.randint, None, lo, hi)


def random_floats(lo, hi):
    return repeatfunc(random.uniform, None, lo, hi)


def random_word(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def random_strings(max_len):
    return map(random_word, random_ints(0, max_len))


def random_list(gen, max_len):
    return list(itertools.islice(gen, 0, random.randint(0, max_len)))


def random_lists(gen, max_len):
    return repeatfunc(lambda: random_list(gen, max_len))


def random_Lists(gen, max_len):
    return map(lambda xs: List(*xs), random_lists(gen, max_len))


def random_ids(gen):
    return map(Id, gen)


def random_maybes(gen):
    return map(lambda x: Just(x) if random.random() <= 0.8 else Nothing, gen)


def random_readers(gen):
    return map(Reader.unit, gen)


def random_states(gen):
    return map(State.unit, gen)


def random_functions(gen):
    return map(lambda x: lambda y: y + x, gen)


def random_state_functions(gen):
    return map(lambda x: lambda s: (s + x, s), gen)


class FunEq:
    def __init__(self, times, gen, cmp_fun=operator.eq):
        self._times = times
        self._gen = gen
        self._cmp_fun = cmp_fun

    def __call__(self, f, g):
        for _ in range(self._times):
            x = next(self._gen)
            if not self._cmp_fun(f(x), g(x)):
                return False
        return True
