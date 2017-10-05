from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws)

from fplib.maybe import Maybe


def test_maybe_monoid():
    xs = random_maybes(random_strings(10))
    monoid_laws(xs, 100)


def test_maybe_functor():
    xs = random_maybes(random_strings(10))
    functor_laws(xs, 100)


def test_maybe_applicative():
    xs = random_maybes(random_strings(10))
    applicative_laws(Maybe, xs, 100)


def test_maybe_monad():
    xs = random_maybes(random_strings(10))
    monad_laws(Maybe, xs, 100)
