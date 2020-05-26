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

# %%
##
project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids.append(project_id)

print(project_ids)

# %%
##
project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
if project_ids['02'] != 'open': # == 'new'
    project_ids['02'] = 'open'

print(project_ids)

# %%
##
item = '001'
items = ['001', '000', '003', '005', '006']

if item in items:
    items.remove(item)
print(items)
