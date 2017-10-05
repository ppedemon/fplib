from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws, trans_laws)

from fplib.list import List
from fplib.transformer import trans
from fplib.maybe_t import MaybeT


T = trans(MaybeT, List)

def cmpt(t0, t1):
    return t0.unwrap == t1.unwrap


def test_maybet_functor():
    xs = map(T.unit, random_strings(10))
    functor_laws(xs, 100, cmp_fun=cmpt)


def test_maybet_applicative():
    xs = map(T.unit, random_strings(10))
    applicative_laws(T, xs, 100, cmp_fun=cmpt)


def test_maybet_monad():
    xs = map(T.unit, random_strings(10))
    monad_laws(T, xs, 100, cmp_fun=cmpt)


def test_maybet_transformer():
    xs = random_Lists(random_strings(10), 10)
    trans_laws(T, xs, 100, cmp_fun=cmpt)
