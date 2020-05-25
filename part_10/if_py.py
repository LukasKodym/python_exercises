# %%
##
filename = '01012020_sales.xlsx'

if filename.endswith('xlsx'):
    print('TAK')
else:
    print('NIE')

# %%
##
code = 'DSVNDOICSN'

if code.isupper():
    print('TAK')
else:
    print('NIE')

# %%
##
number = 1.0

if isinstance(number, int):
    print('TAK')
else:
    print('NIE')

# %%
##
password = 'cskdnjcasa#!'

if len(password) >= 11:
    print('Hasło poprawne')
else:
    print('Hasło zbyt któtkie')

# %%
##
password = 'cskdnjcasa#!'
# print('Hasło poprawne' if password.find('!') > 0 and len(password) >= 11 else 'Hasło niepoprawne')
print('Hasło poprawne' if '!' in password and len(password) >= 11 else 'Hasło niepoprawne')
