# %%
##
with open('part_23/gaming.txt', 'r') as file:
    text = file.readlines()

res = [line.replace("\n", "") for line in text if line.strip() != '']

print(res)

# %%
##
tax = 0.23
net_price = [5.5, 4.0, 9.0, 10.0]

gross_price = [round(item * (1 + tax), 2) for item in net_price]
print(gross_price)

# %%
##
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

res = [round(pv * (1 + item) ** n, 2) for item in rate]
print(res)

# %%
##
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

res = [round(pv * ((1 + item) ** n - 1), 2) for item in rate]
print(res)

# %%
##
with open('part_23/plw.txt', 'r') as f:
    lines = f.read().splitlines()

res = [line.split() for line in lines if line.strip() != '']

print(res)
