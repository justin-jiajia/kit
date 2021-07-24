def ftoc(f):
    c = f - 32
    c = c / 1.8
    return c


def ctof(c):
    f = c * 1.8
    f = 32 + f
    return f
