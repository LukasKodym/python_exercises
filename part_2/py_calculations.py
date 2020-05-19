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
