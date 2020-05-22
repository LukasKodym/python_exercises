# %%
##
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
print(wig20 + mwig40)

# %%
##
wig20 = ('CDR', 'PKO', 'PEO')
mwig40 = ('PLW', 'AMC', 'BFT')
result = (wig20, mwig40)
print(result)

# %%
##
members = (('Kasia', 23), ('Tomek', 19))
result = (members[0], ('Adam', 26), members[1])
print(result)

# %%
##
default = ('YES', 'NO', 'NO', 'YES', 'NO')
print(f'Liczba wystąpień: {default.count("YES")}')

# %%
##
names = ('Monika', 'Tomek', 'Adam', 'Olaf')
sorted_names = tuple(sorted(names))
# print((names[2], names[0], names[3], names[1]))
print(sorted_names)

# %%
##
from operator import itemgetter

info = (('Monika', 19), ('Tomek', 21), ('Adam', 18))

rosnaco = tuple(sorted(info, key=itemgetter(1)))
malejaco = tuple(sorted(info, key=itemgetter(1), reverse=True))
print(f'Rosnąco: {rosnaco}')
print(f'Malejąco: {malejaco}')

# another way: key=lambda item: item[1]

# %%
##
stocks = (('Playway', ('PLW', 310)), ('CD Projekt', ('CDR', 300)))
print(stocks[0][1][0])
