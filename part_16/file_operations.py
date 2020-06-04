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
with open('part_16\\plw_d.csv', 'r') as file:
    content = file.read().splitlines()
res = {}

for idx, line in enumerate(content):
    if idx == 0:
        res.setdefault(line.split(',')[0])
        res.setdefault(line.split(',')[-2])
    if idx > 0:
        res['Data'] = [line.split(',')[0] for idx, line in enumerate(content) if idx > 0]
        res['Zamkniecie'] = [float(line.split(',')[-2]) for idx, line in enumerate(content) if idx > 0]

print(res)

# %%
##
with open('part_16\\plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [(line.split(',')[0], line.split(',')[4]) for line in content]
result = {
    data[0][0]: [data[1:][i][0] for i in range(len(data) - 1)],
    data[0][1]: [float(data[1:][i][1]) for i in range(len(data) - 1)]
}
print(result)

# %%
##
with open('part_16\\plw_d.csv', 'r') as file:
    content = file.read().splitlines()

data = [int(line.split(',')[5]) for line in content[1:]]
print(f'Max Vol: {max(data)}')

# %%
##
with open('part_16\\plw_d.csv', 'r') as f:
    content = f.read().splitlines()

val = []
data = []

for line in content[1:]:
    val.append(int(line.split(',')[5]))

idx = val.index(max(val))

for line in content[1:]:
    data.append(line.split(',')[0])

print(f'Data: {data[idx]}')
