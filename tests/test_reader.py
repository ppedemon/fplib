from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws)

from fplib.reader import Reader


def test_reader_functor():
    xs = random_readers(random_strings(10))
    functor_laws(xs, 100, cmp_fun=FunEq(50, random_ints(0, 100)))


def test_reader_applicative():
    xs = random_readers(random_strings(10))
    applicative_laws(Reader, xs, 50, cmp_fun=FunEq(50, random_ints(0, 100)))


def test_reader_monad():
    xs = random_readers(random_strings(10))
    monad_laws(Reader, xs, 50, cmp_fun=FunEq(50, random_ints(0, 100)))
