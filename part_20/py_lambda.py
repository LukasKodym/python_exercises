# %%
##
stocks = ['playway', 'boombit', 'cd projekt']

length = list(map(lambda item: len(item), stocks))
print(length)


# %%
##


def sort_list(lst):
    return sorted(lst, key=lambda x: x[1])


my_list = [(2, 7), (7, 4), (8, 1)]
print(sort_list(my_list))

# %%
##
func_2 = lambda x, y: x + y + 2

print(func_2(3, 6))

# %%
##
items = [(3, 4), (2, 5), (1, 4), (6, 1)]

items.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
print(items)

# %%
##
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

stocks.sort(key=lambda stock: stock['price'])

print(stocks)

# %%
##
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

res = list(filter(lambda item: item['indeks'] == 'mWIG40', stocks))

print(res)

# %%
##
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

res = list(map(lambda x: x['indeks'] == 'mWIG40', stocks))

print(res)

# %%
##
items = ['P-1', 'R-2', 'D-4', 'F-6']

# new_items = list(map(lambda item: str.replace(item, '-', ''), items))
new_items = list(map(lambda item: item.replace('-', ''), items))

print(new_items)

# %%
##
num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

res = list(map(lambda n1, n2: n1 % n2, num1, num2))

print(res)
