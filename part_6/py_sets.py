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
val.remove(' ')
val.remove('.')
val.difference_update(vowels)
print(f'Liczba elementów: {len(val)}')

# or
# %%
##
text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set(text.lower().replace(' ', '').replace('.', ''))
letters.difference_update(vowels)
print(f'Liczba elementów: {len(letters)}')

# %%
##
A = {2, 4, 6, 8}
B = {4, 10}
C = A.symmetric_difference(B)
print(f'Róznica symetryczna: {C}')

# %%
##
ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
add = ad1_id.symmetric_difference(ad2_id)
print(f'Wybrane ID: {add}')

# %%
##
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
result = is_clicked.intersection(is_bought)
print(f'ID klientów: {result}')
