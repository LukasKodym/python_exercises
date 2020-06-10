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
