# %%
##
x = -1.5
expression = 'x**2 + x'

res = eval(expression)

print(res)

# %%
##
var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1, tuple))
print(isinstance(var2, tuple))
print(isinstance(var3, tuple))
print(isinstance(var4, tuple))
print(isinstance(var5, tuple))

# %%
##
characters = ['k', 'b', 'c', 'j', 'z', 'w']
# characters.sort()
print(f'Pierwsza: {min(characters)}')
print(f'Ostatnia: {max(characters)}')

# %%
##
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

new_lst = list(zip(ticker, full_name))
print(new_lst)

# %%
##
items = (' ', '0', 0.1, True)

print(all(items))

# %%
##
items = ('', 0.0, 0, False)

print(any(items))

# %%
##
number = 234
print(bin(number)[2:].count('1'))
