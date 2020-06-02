# %%
##
with open('part_16\\playway.txt', 'r') as f:
    lines = f.read().splitlines()

close = []

for idx, line in enumerate(lines):
    if idx > 0:
        close.append(int(line.split(',')[-2]))

res = sum(close) / len(close)

print(f'3-dniowa średnia cena zamknięcia: {res:.2f}')

# %%
##

try:
    with open('part_16\\indeks.txt', 'r') as f:
        lines = f.readlines()

except FileNotFoundError:
    print('Brak pliku')

res = []
try:
    for line in lines:
        if line.startswith('WIG'):
            res.append(line.replace('\n', ''))
except NameError:
    print('Błąd zmiennej')
print(res)

#     lines = f.read().splitlines()
#
# res = [line for line in lines if res.startswith('WIG')]

# %%
##
