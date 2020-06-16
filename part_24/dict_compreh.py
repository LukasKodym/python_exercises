# %%
##
res = {x: x ** 2 for x in range(1, 8)}

print(res)

# %%
##
stocks = ['Playway', 'CD Projekt', 'Boombit']

res = {s: len(s) for s in stocks}

print(res)

# %%
##
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}

res = {val: key for (key, val) in stocks.items()}

print(res)

# %%
##
stocks = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}

res = {k: v for k, v in stocks.items() if v > 100}

print(res)

# %%
##
res = [{i: i ** k for i in range(1, 10)} for k in range(1, 4)]

print(res)

# %%
##
indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['liczba spółek', 'spółki', 'kapitalizacja']

res = {i: {p: None for p in properties} for i in indeks}

print(res)

# %%
##
indeks = ['WIG20', 'mWIG40', 'sWIG80']

res = {k: indeks[k] for k in range(0, len(indeks))}

print(res)
