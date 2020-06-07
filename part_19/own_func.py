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


# %%
##


def map_longest(iter_obj):
    res = []
    for item in iter_obj:
        res.append(len(item))
    return max(res)


# %%
##


def filter_ge_6(iter_obj):
    res = []
    for item in iter_obj:
        if len(item) >= 6:
            res.append(item)
    return res


# %%
##


def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
        i -= 1
    return res


# solution with recurrence function


def factorial_2(n):
    if n == 0:
        return 1
    return n * factorial_2(n - 1)


# %%
##


def count_str(iter_obj):
    res = []
    for item in iter_obj:
        if isinstance(item, str):
            res.append(item)
    return len(res)


# %%
##


def count_str_2(iter_obj):
    res = []
    for item in iter_obj:
        if isinstance(item, str) and len(item) > 2:
            res.append(item)
    return len(res)


# %%
##


def remove_duplicates(iter_obj):
    res = []
    for item in set(iter_obj):
        res.append(item)
    return res


"""
def remove_duplicates(iter_obj):
    return list(set(iter_obj))
"""


# %%
##


def is_distinct(obj):
    if len(obj) == len(set(obj)):
        return True
    else:
        return False


"""
def is_distinct(obj):
    return len(obj) == len(set(obj))
"""


# %%
##


def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)


function(3)
function(5, ['a', 'b', 'c'])
function(6)
