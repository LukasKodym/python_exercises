# %%
##
omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_gt_10 = {pair for pair in omega if pair[0] + pair[1] > 10}
print(f'P-stwo: {len(sum_gt_10) / len(omega):.2f}')

# %%
##
desc = "Playway: Playway to producent gier komputerowych."

res = desc.lower().replace(':', '').replace('.', '').split()

print(len({word for word in res}))

# %%
##

omega = {(i, j) for i in range(1, 7) for j in range(1, 7)}
sum_sq_get_45 = {pair for pair in omega if pair[0] ** 2 + pair[1] ** 2 >= 45}
print(f'P-stwo: {len(sum_sq_get_45) / len(omega):.2f}')

# %%
##
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
trio_of_7 = {(x, y, z) for (x, y, z) in omega if (x + y + z) % 7 == 0}
print(f'P-stwo: {len(trio_of_7) / len(omega):.2f}')

# %%
##
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
res = {(x, y, z) for (x, y, z) in omega if (x ** 2 + y ** 2 + z ** 2) % 3 == 0}
print(f'P-stwo: {len(res) / len(omega):.4f}')

# %%
##
omega = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
res = {(x, y, z) for (x, y, z) in omega if x % 2 != 0 and y % 2 != 0 and z % 2 != 0}
prob = round(len(res) / len(omega), 3)
print(f'P-stwo: {prob}')
