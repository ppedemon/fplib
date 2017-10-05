from generators import *
from laws import (monoid_laws, functor_laws, applicative_laws, monad_laws, trans_laws)

from fplib.maybe import Maybe
from fplib.transformer import trans
from fplib.ident_t import IdT


T = trans(IdT, Maybe)

def cmpidt(idt0, idt1):
    return idt0.unwrap == idt1.unwrap


def test_idt_functor():
    xs = map(T.unit, random_strings(10))
    functor_laws(xs, 100, cmp_fun=cmpidt)


def test_idt_applicative():
    xs = map(T.unit, random_strings(10))
    applicative_laws(T, xs, 100, cmp_fun=cmpidt)


def test_idt_monad():
    xs = map(T.unit, random_strings(10))
    monad_laws(T, xs, 100, cmp_fun=cmpidt)


def test_idt_transformer():
    xs = random_maybes(random_strings(10))
    trans_laws(T, xs, 100, cmp_fun=cmpidt)
