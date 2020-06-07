# %%
##


def maximum(a, b):
    if a > b:
        return a
    else:
        return b


# %%
##


def maximum_2(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


# %%
##


def multi(iter_obj):
    val = 1
    for i in iter_obj:
        val *= i
    return val


