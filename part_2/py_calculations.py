# %%
##
pi = 3.14
print('Pole koła wynosi: {} cm2'.format(pi * 5 ** 2))

# %%
##
amount = 1000
rate = 0.03
i = 1

for i in range(5):
    amount = amount * rate + amount
    i += 1

print(f'Wartość końcowa inwestycji wynosi: {round(amount, 2)} PLN')

# %%
##
amount = 1000
rate = 0.03
time = 5
end_value = amount * (1 + rate) ** time
print(f'Wartość końcowa inwestycji wynosi: {end_value:.2f} PLN')

# %%
##
a = 3
b = -4
c = 1
delta = b ** 2 - 4 * a * c
print(f'Delta wynosi: {delta}')

# %%
##
a_1 = 14
a_10 = 50
n = 10
end_value = (a_1 + a_10) / 2 * n
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {end_value}')

# %%
##
a_1 = 8 * 2 ** (1 - 1)
a_2 = 8 * 2 ** (2 - 1)
q = a_2 / a_1
end_value = a_1 * (1 - q ** 6) / (1 - q)
print(f'Suma pierwszych 6 wyrazów ciągu wynosi: {end_value}')

# %%
##
a = 1
b = 5
c = 4
print(f'x1+x2 = {- b / a}\nx1x2 = {c / a}')

# %%
##
a_x, a_y = 2, 4
b_x, b_y = -4, 6
s_x, s_y = (a_x + b_x) / 2, (a_y + b_y) / 2,
print(f'Środek odcinka AB: ({s_x}, {s_y})')

# %%
##
a_x, a_y = 3, 2
b_x, b_y = -1, -1
d = (((b_x - a_x) ** 2 + (b_y - a_y) ** 2)) ** (1 / 2)
print(f'Odległość punktów A i B wynosi: {d}')
