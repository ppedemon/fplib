from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws)


def test_ident_functor():
    xs = random_ids(random_strings(10))
    functor_laws(xs, 100)


def test_ident_applicative():
    xs = random_ids(random_strings(10))
    applicative_laws(Id, xs, 100)


def test_ident_monad():
    xs = random_ids(random_strings(10))
    monad_laws(Id, xs, 100)
