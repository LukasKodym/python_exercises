# %%
##
suma = 3000
counter = 0

try:
    res = suma / counter
except ZeroDivisionError:
    print('Dzielenie przez zero.')

# %%
##
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('Nie znaleziono pliku.')

# %%
##
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    print(f'Klucz {user_id} nie występuje w słowniku. Dodawanie klucza...')
    users.setdefault('004')
    print(users)
