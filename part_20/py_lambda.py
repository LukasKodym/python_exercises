# %%
##
stocks = ['playway', 'boombit', 'cd projekt']

length = list(map(lambda item: len(item), stocks))
print(length)


# %%
##


def sort_list(lst):
    return sorted(lst, key=lambda x: x[1])


# %%
##


func_2 = lambda x, y: x + y + 2

# %%
##
items = [(3, 4), (2, 5), (1, 4), (6, 1)]

items.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
print(items)

# &&
##