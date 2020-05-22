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
