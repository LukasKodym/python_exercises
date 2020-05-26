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
result = []
for word in words:
    word.lower().replace(',', '').replace('.', '')
    for word_2 in words:
        if len(word_2) > 10:
            result.append(word_2)
print(result)

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
    idx.find()
