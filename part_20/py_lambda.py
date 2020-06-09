# %%
##
stocks = ['playway', 'boombit', 'cd projekt']

length = list(map(lambda item: len(item), stocks))
print(length)

# %%]
##


def sort_list(lst):
    return sorted(lst, key=lambda x: x[1])
