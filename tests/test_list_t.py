from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws, trans_laws)

from fplib.maybe import Maybe
from fplib.transformer import trans
from fplib.list_t import ListT


T = trans(ListT, Maybe, 'ListT[Maybe]')

def cmpt(t0, t1):
    return t0.unwrap == t1.unwrap


def test_listt_functor():
    xs = map(T.unit, random_strings(10))
    functor_laws(xs, 100, cmp_fun=cmpt)


def test_listt_applicative():
    xs = map(T.unit, random_strings(10))
    applicative_laws(T, xs, 100, cmp_fun=cmpt)


def test_listt_monad():
    xs = map(T.unit, random_strings(10))
    monad_laws(T, xs, 100, cmp_fun=cmpt)


def test_listt_transformer():
    xs = random_maybes(random_strings(10))
    trans_laws(T, xs, 100, cmp_fun=cmpt)
