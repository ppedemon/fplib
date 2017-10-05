from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws)

from fplib.list import List


def test_list_monoid():
    xs = random_Lists(random_strings(10), 20)
    monoid_laws(xs, 100)


def test_list_functor():
    xs = random_Lists(random_strings(10), 20)
    functor_laws(xs, 100)


def test_list_applicative():
    xs = random_Lists(random_strings(10), 20)
    applicative_laws(List, xs, 100)


def test_list_monad():
    xs = random_Lists(random_strings(10), 20)
    monad_laws(List, xs, 100)
