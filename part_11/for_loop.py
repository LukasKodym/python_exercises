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
items = list(dict.fromkeys(items))
print(items)
# or
result = []
for i in items:
    if i not in result:
        result.append(i)
print(result)

# %%
##
text = 'Python jest bardzo popularnym językiem programowania'
words = text.split(' ')
tmp = []
for i in words:
    if len(tmp) < 4:
        tmp.append(i.lower())
print(tmp)

# or
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)

# %%
##
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
res = []
for item in probabilities:
    if item >= 0.5:
        res.append(item)
print(res)

# %%
##
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []
for prob in probabilities:
    if prob < 0.5:
        result.append(0)
    elif prob >= 0.5:
        result.append(1)
print(result)

# %%
##
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = {}
for item in items:
    if item == item:
        result.setdefault(item, items.count(item))

print(result)

# or
freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1

print(freq)

# %%
##
text = """Python – język programowania wysokiego poziomu
ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek
standardowych, którego ideą przewodnią jest czytelność i
klarowność kodu źródłowego."""
new = text.replace('– ', '').replace(',', '').replace('.', '').replace('\n', ' ')
words = new.split(' ')
result = []
for word in words:
    if len(word) > 10:
        result.append(word.lower())
print(result)

# or
words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 10]
print(words)

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

for idx in indexes:
    if idx.count('20') > 0:
        print(idx)
    elif idx.count('30') > 0:
        print(idx)
# or
for index in indexes:
    if '20' in index or '30' in index:
        print(index)

# %%
##
gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}
for k, v in gaming.items():
    if v > 100:
        print(k)

# %%
##
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for name in names:
    if name.isalpha():
        print(f'Hello {name}!')
