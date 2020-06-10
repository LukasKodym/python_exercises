# %%
##


def file_gen(lst):
    for item in lst:
        if item.endswith('.txt'):
            yield item

# %%
##


def enum(lst):
    counter = range(len(lst))
    for item in lst:
        yield tuple(counter) + item
