from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws)

from fplib.state import State


def test_state_functor():
    xs = random_states(random_strings(10))
    functor_laws(xs, 100, cmp_fun=FunEq(50, random_ints(0, 100)))


def test_state_applicative():
    xs = random_states(random_strings(10))
    applicative_laws(State, xs, 50, cmp_fun=FunEq(50, random_ints(0, 100)))


def test_state_monad():
    xs = random_states(random_strings(10))
    monad_laws(State, xs, 50, cmp_fun=FunEq(50, random_ints(0, 100)))
