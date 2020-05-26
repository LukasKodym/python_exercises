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

# or
list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
for item in list1:
    if item in list2:
        print(True)
        break

# %%
##
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
res = True

for item in hashtags:
    if not isinstance(item, str):
        res = False
        break
print(res)

# %%
##
number = 13

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} nie jest liczbą pierwszą')
            break
    else:
        print(f'{number} - liczba pierwsza')
else:
    print(f'{number} nie jest liczbą pierwszą')
