# %%
##

tup = (1, 5, 8, 'f', 'abc', 87)
print(tup)

print(tuple(enumerate(tup)))

print(type(dict(enumerate(tup))))

# %%
##
lst = list(tup)
print(lst)

print(dict(enumerate(lst)))

# %%
##
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]
print(list(enumerate(ticker)))

# %%
##
password = 'cskdnjcasa#!'
password.find('?')
bool(password.find('?') > 0)

# %%
##
project_ids = {
    '01': 'open',
    '02': 'new',
    '03': 'in progress',
    '04': 'completed'
}
print(project_ids['02'])

# %%
##
if project_ids['02'] != 'open':
    project_ids['02'] = 'open'

# %%
##
for char in zip('abcde', '12345'):
    print(char)

for char, num in zip('abcde', '12345'):
    print(char, num)

# %%
##
ticker = [1, 5, 6, 99, 7]
for i in ticker:
    print(type(i), ': ', i)
tmp = []
print(ticker)
for i in ticker:
    tmp.append(str(i))
ticker = tmp

for i in ticker:
    print(type(i), ': ', i)

print('aaaa'.join(ticker))

# %%
##
items = [1, 5, 3, 2, 2, 4, 2, 4]
tmp = (dict.fromkeys(items))
print(tmp)

# %%
##
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
tmp = []
[tmp.append(i) for i in probabilities if i >= 0.5]
print(tmp)

# %%
##
text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
words = text.split()
# result = []
# for word in words:
#     word.lower().replace(',', '').replace('.', '')
#     for word_2 in words:
#         if len(word_2) > 10:
#             result.append(word_2)
# print(result)

# %%
##
indexes = [
    'WIG', 'WIG-banki', 'WIG-budownictwo', 'WIG-CEE',
    'WIG-chemia', 'WIG-energia', 'WIG-ESG', 'WIG-górnictwo',
    'WIG-informatyka', 'WIG-leki', 'WIG-media', 'WIG-motoryzacja',
    'WIG-nieruchomości', 'WIG-odzież', 'WIG-paliwa', 'WIG-Poland',
    'WIG-spożywczy', 'WIG-telekomunikacja', 'WIG-Ukraine',
    'WIG.GAMES', 'WIG.MS-BAS', 'WIG.MS-FIN', 'WIG.MS-PET',
    'WIG20', 'WIG20dvp', 'WIG20lev', 'WIG20short', 'WIG20TR',
    'WIG30', 'WIG30TR', 'WIGdiv', 'WIGtech'
]
#
# for idx in indexes:
#     idx.find()

# %%
##
a = 'aaa'
print(bool(isinstance(a, str)))

# %%
##
hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
res = False

for item in hashtags:
    if item is str:
        res = True
        break
print(res)

# %%
##
for number in range(0, 1000, 1):
    print(number)

# %%
##
tmp = []
number = 0

while len(tmp) < 10:
    # for number in range(0,30,1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            tmp.append(str(number))
    number += 1

print(','.join(tmp))

# %%
##
derivative = lambda w: 2 * w - 4
print(derivative(5))

# %%
##
n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')

# %%
##
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)

# %%
##
import csv

lines = [['Bob', 'male', '27'],
         ['Smith', 'male', '26'],
         ['Alice', 'female', '26']]

header = ['name', 'gender', 'age']

with open("test.csv", "w", newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)  # write the header
    # write the actual content line by line
    for l in lines:
        writer.writerow(l)
    # or we can write in a whole
    # writer.writerows(lines)

# %%
##
number = 234
binary = bin(number)
print(type(binary))
binary = binary[2:]
print(binary.count('1'))

# %%
##
txt = 'rower'

print(txt[::-1])

# %%
##
print(4 // 3)

# %%
##
lst = [2, 6, 1, 9, 5]


def dub(ls):
    res = []
    for i in ls:
        var = (i * 2)
        res.append(var)
    return res


print(dub(lst))


# %%
##


def func_1(a, b):
    return a + b + 2


# %%
##


string = '     @@@Lukas and Mark@@@     '
print(string.strip())

# %%
##
pv = 1000
n = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]

res = []

for r in rate:
    a = round(pv * (1 + r) ** n, 2)
    res.append(a)

print(res)

# %%
## zadanie matura 2020


# def czy_podobne(n, A, B, k):
#     for i in range(1, k + 1):
#         if A[i] != B[n - k + i]:
#             return 'FAŁSZ'
#     for i in range(k + 1, n + 1):
#         if A[i] != B[i - k]:
#             return 'FAŁSZ'
#     return 'PRAWDA'
#
#
# czy_podobne(3, [5, 7, 9], [5, 7, 9], 0)

# %%
##
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]

for i, j in zip(y_true, y_pred):
    sum = 0
    sum += abs(i - j)
print(sum)

print("\n")

for i in zip(y_true, y_pred):
    p = 0
    p += abs(i[0] - i[1])
print(p)

# %%
##
items = [3, 4, 0, 2, 0, 5, 1, 6, 2]


def transfer_zeros(items):
    result = []
    counter = 0
    for item in items:
        if item == 0:
            counter += 1
        else:
            result.append(item)
    result.extend([0] * counter)
    return result


transfer_zeros(items)


# %%
##


def arange(start, stop, step=1):
    collect = start
    res = []
    while collect < stop:
        if stop > start:
            res.append(collect)
            collect += step
        return res


arange(1, 6, 3)

# %%
##
l_1 = [[1], [2]]
l_2 = [[3], [4]]


def concat(l1, l2):
    res = []
    for i, j in zip(l1, l2):
        con = i + j
        res.append(con)
    return res


concat(l_1, l_2)

# %%
##
array = [[0.3, 0.4, 0.3], [0.0, 0.1, 0.9]]

print(max(array[1]))
