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
