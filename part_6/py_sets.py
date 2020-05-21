# %%
##
przedmioty = {'matematyka', 'polski'}
przedmioty.add('angielski')
print(przedmioty)

# %%
##
text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
val = set(text.lower())
print(val)
val.remove(' ')
print(val)
y = val.remove('.')
print(val)
x = val.intersection(vowels)
print(x)
val.remove(x)
print(val)

# %%
##
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}