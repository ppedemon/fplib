from generators import *
from laws import monoid_laws
from pytest import approx

from fplib.list import List


def test_int_monoid():
    xs = random_ints(0, 1000)
    monoid_laws(xs, 100)


def test_float_monoid():
    xs = random_floats(0.0, 10.0)
    monoid_laws(xs, 100, cmp_fun=lambda x, y: x == approx(y))


def test_str_monoid():
    xs = random_strings(20)
    monoid_laws(xs, 100)


def test_list_monoid():
    xs = random_lists(random_strings(10), 20)
    monoid_laws(xs, 100)
