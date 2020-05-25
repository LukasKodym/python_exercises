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

# %%
##
project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
print(project_ids['02'])

# %%
##
if project_ids['02'] != 'open':
    project_ids['02'] = 'open'

# %%
##
for char in zip('abcde', '12345'):
    print(char)

for char, num in zip('abcde', '12345'):
    print(char, num)

# %%
##
ticker = [1, 5, 6, 99, 7]
for i in ticker:
    print(type(i), ': ', i)
tmp = []
print(ticker)
for i in ticker:
    tmp.append(str(i))
ticker = tmp

for i in ticker:
    print(type(i), ': ', i)

print('aaaa'.join(ticker))
