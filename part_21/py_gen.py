# %%
##


def file_gen(lst):
    for item in lst:
        if item.endswith('.txt'):
            yield item


# %%
##


def enum(lst):
    counter = 0
    for item in lst:
        yield counter, item
        counter += 1


# %%
##


def dayname(idx):
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    yield days[idx - 1]
    yield days[idx]
    yield days[(idx + 1) % 7]


for pair in dayname(5):
    print(pair)
