# %%
##
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
res = False

for item in list1:
    if item in list2:
        res = True
        break

print(res)
