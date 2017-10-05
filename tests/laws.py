import itertools
import operator

from fplib.functor import unit
from fplib.misc import (compose, ident)
from fplib.monoid import zero

from generators import *


"""
Monoid Laws: associativity and left + right identities.
"""
def monoid_assoc(x, y, z, cmp_fun=operator.eq):
    assert cmp_fun((x + y) + z, x + (y + z))

def monoid_left_ident(x, cmp_fun=operator.eq):
    z = zero(x.__class__)
    assert cmp_fun(z + x, x)

def monoid_right_ident(x, cmp_fun=operator.eq):
    z = zero(x.__class__)
    assert cmp_fun(x + z, x)

def monoid_laws(testdata, ntests, cmp_fun=operator.eq):
    for i in range(ntests):
        x, y, z = itertools.islice(testdata, 0, 3)
        monoid_assoc(x, y, z, cmp_fun)
        monoid_left_ident(x, cmp_fun)
        monoid_right_ident(y, cmp_fun)


"""
Functor laws: identity and composition.
"""
def fun_ident(functor, cmp_fun=operator.eq):
    assert cmp_fun(ident >> functor, ident(functor))

def fun_comp(functor, f, g, cmp_fun=operator.eq):
    assert cmp_fun(compose(f, g) >> functor, f >> (g >> functor))

def functor_laws(functor_gen, ntests, cmp_fun=operator.eq):
    f = lambda x: x * 2
    g = len
    for functor in itertools.islice(functor_gen, 0, ntests):
        fun_ident(functor, cmp_fun)
        fun_comp(functor, f, g, cmp_fun)


"""
Applicative laws: identity, homomorphism, exchange, and composition.
"""
def app_ident(app, cmp_fun=operator.eq):
    return cmp_fun(unit(app.__class__, ident) & app, app)

def app_homo(A, f, x, cmp_fun=operator.eq):
    return cmp_fun(unit(A, f) & unit(A, x), unit(A, f(x)))

def app_xchg(appfun, x, cmp_fun=operator.eq):
    A = appfun.__class__
    return cmp_fun(appfun & unit(A, x), unit(A, lambda f: f(x)) & appfun)

def app_comp(appf, appg, appx, cmp_fun=operator.eq):
    return cmp_fun(unit(appf.__class__, compose) & appf & appg & appx, appf & (appg & appx))

def applicative_laws(A, app_gen, ntests, cmp_fun=operator.eq):
    f = lambda x: x * 2
    g = len
    appf = unit(A, f)
    appg = unit(A, g)

    for i in range(ntests):
        app_homo(A, f, i, cmp_fun)
        app_xchg(appf, i, cmp_fun)

    for app in itertools.islice(app_gen, 0, ntests):
        app_ident(app, cmp_fun)
        app_comp(appf, appg, app, cmp_fun)


"""
Monad laws: associativity and left + right identities
"""
def monad_left_ident(M, x, f, cmp_fun=operator.eq):
    assert cmp_fun(unit(M, x) >> f, f(x))

def monad_right_ident(m, cmp_fun=operator.eq):
    assert cmp_fun(m >> (lambda x: unit(m.__class__, x)), m)

def monad_assoc(m, f, g, cmp_fun=operator.eq):
    assert cmp_fun(m >> g >> f, m >> (lambda x: g(x) >> f))

def monad_laws(M, mon_gen, ntests, cmp_fun=operator.eq):
    f = lambda x: unit(M, x * 2)
    g = lambda x: unit(M, len(x))

    for i in range(ntests):
        monad_left_ident(M, i, f, cmp_fun)

    for m in itertools.islice(mon_gen, 0, ntests):
        monad_right_ident(m, cmp_fun)
        monad_assoc(m, f, g, cmp_fun)


"""
Transformer laws: associativity and identity
"""
def trans_ident(T, x, cmp_fun=operator.eq):
    assert cmp_fun(T.lift(T.innermonad.unit(x)), T.unit(x))

def trans_assoc(T, m, f, cmp_fun=operator.eq):
    assert cmp_fun(T.lift(m >> f), T.lift(m) >> compose(T.lift, f))

def trans_laws(T, mon_gen, ntests, cmp_fun=operator.eq):
    for i in range(ntests):
        trans_ident(T, i, cmp_fun)

    f = lambda x: unit(T.innermonad, len(x))
    for m in itertools.islice(mon_gen, 0, ntests):
        trans_assoc(T, m, f, cmp_fun)
