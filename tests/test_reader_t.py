from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws, trans_laws)

from fplib.maybe import Maybe
from fplib.transformer import trans
from fplib.reader_t import ReaderT


T = trans(ReaderT, Maybe, 'ReaderT[Maybe]')

def cmpt(t0, t1):
    return FunEq(50, random_ints(0, 100))(t0, t1)


def test_readert_functor():
    xs = map(T.unit, random_strings(10))
    functor_laws(xs, 50, cmp_fun=cmpt)


def test_readert_applicative():
    xs = map(T.unit, random_strings(10))
    applicative_laws(T, xs, 50, cmp_fun=cmpt)


def test_readert_monad():
    xs = map(T.unit, random_strings(10))
    monad_laws(T, xs, 50, cmp_fun=cmpt)


def test_readert_transformer():
    xs = random_maybes(random_strings(10))
    trans_laws(T, xs, 50, cmp_fun=cmpt)
