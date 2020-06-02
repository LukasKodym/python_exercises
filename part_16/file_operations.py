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
