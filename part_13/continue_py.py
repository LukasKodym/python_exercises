# %%
##
gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for key, value in gaming.items():
    if value[1] == 'PLN':
        continue
    else:
        value[0] *= 4.0
        value[1] = 'PLN'

print(gaming)

# %%
##
names = ['Jack', 'Leon', 'Alice', None, 'Bob']

for name in names:
    if not isinstance(name, str):
        continue
    else:
        print(name)
