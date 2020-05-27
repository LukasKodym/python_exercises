# %%
##
tmp = []
counter = 0

while counter < 10:
    for number in range(0, counter + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
        else:
            tmp.append(str(number))
        counter = len(tmp)
print(','.join(tmp))

# %%
##
counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))
