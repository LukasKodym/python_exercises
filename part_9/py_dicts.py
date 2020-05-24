# %%
##
cities = {'Poland': 'Warsaw',
          'Germany': 'Berlin',
          'Austria': 'Vienna'}

print(cities)

# %%
##
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.keys())

# %%
##
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.values())

# %%
##
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'}
print(capitals.items())

# %%
##
capitals = {
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Vienna'}
print(capitals.get('Austria'))

# %%
##
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks.get('PLW'))
# or
print(stocks['PLW'])

# %%
##
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks['TEN']['Ten Square Games'])

# %%
##
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
stocks['CDR']['CD Projekt'] = 310
print(stocks['CDR'])

# %%
##
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}
print(stocks)
stocks['BBT'] = {'Boombit': 23}
print(stocks.values())

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
ticker = [
    'ALR', 'CCC', 'CDR', 'CPS', 'DNP',
    'JSW', 'KGH', 'LPP', 'LTS', 'MBK',
    'OPL', 'PEO', 'PGE', 'PGN', 'PKN',
    'PKO', 'PLY', 'PZU', 'SPL', 'TPE'
]

print(dict(enumerate(ticker)))

# %%
##
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
print(list(sorted(set(project_ids.values()))))

# %%
##
stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
stats.pop('ruch')
# del stats['ruch']
print(stats)

# %%
##
users = {'001': 'Marek', '002': 'Monika', '003': 'Jakub'}
print(users.get('004', 'nieokreślony'))
