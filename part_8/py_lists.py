# %%
##
cities = ['Warszawa', 'Łódź', 'Kraków']
print(cities)
cities.append("Gdańsk")
print(cities)

# %%
##
idx = ['001', '002', '001', '003', '001']
result = idx.count('001')
print(f'Liczba wystąpień: {result}')

# %%
##
text = 'Programowanie w języku Python'
new_list = list(set(text.lower().replace('ę', 'e')))
new_list.remove(' ')
new_list.sort()
print(new_list[:10])

# %%
##
filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)

# %%
##
day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

# %%
##
techs = ('python', 'java', 'sql', 'aws')
techs = tuple(sorted(techs))
print(techs)

# %%
##
hashtags = ['summer', 'time', 'vibes']
new = '#' + '#'.join(hashtags)
print(new)
