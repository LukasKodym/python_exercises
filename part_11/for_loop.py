# %%
##
result = ''
for i in range(1, 100):
    if i % 11 == 0:
        result += str(i) + ','
print(result[:len(result) - 1])

# or better solution

result = []
for i in range(1, 100):
    if i % 11 == 0:
        result.append(str(i))
print(','.join(result))

# %%
##
result = []
for i in range(10, 99):
    if i % 11 == 0 and i % 3 != 0:
        result.append(str(i))
print(','.join(result))

# %%
##
items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
tmp = []
for i in items:
    if i % 2 == 0:
        tmp.append(i)
print(tmp)

# %%
##
items = [1, 5, 3, 2, 2, 4, 2, 4]
res = []
for i in items:
    if items[i] != items[]:
        res.append(i)
print(res)

