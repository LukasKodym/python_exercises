# %%
##
stocks = ['playway', 'boombit', 'cd projekt']

length = list(map(lambda item: len(item), stocks))
print(length)

# %%]
##
lst = [(1, 3), (4, 2), (6, 1)]

# print(lst[:3][1:])

sort_list = list(map(lambda item: item[1]), lst)

print(sort_list)
