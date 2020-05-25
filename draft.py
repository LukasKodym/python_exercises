# %%
##

tup = (1, 5, 8, 'f', 'abc', 87)
print(tup)

print(tuple(enumerate(tup)))

print(type(dict(enumerate(tup))))

# %%
##
lst = list(tup)
print(lst)

print(dict(enumerate(lst)))

# %%
##
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]
print(list(enumerate(ticker)))

# %%
##
password = 'cskdnjcasa#!'
password.find('?')
bool(password.find('?') > 0)
