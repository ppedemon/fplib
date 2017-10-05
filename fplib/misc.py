from fplib.curry import curry

def fail(x):
    raise ValueError(x)

def ident(x):
    return x

@curry
def compose(f, g, x):
    return f(g(x))

@curry
def const(x, y):
    return x
