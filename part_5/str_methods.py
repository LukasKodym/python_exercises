# %%
##
text = 'python jest popularnym językiem programowania.'
print(text.capitalize())

# %%
##
text = 'python jest popularnym językiem programowania.'
# p = text.count('p')
print(f'Liczba wystąpień: {text.count("p")}')

# %%
##
code1 = 'FVNISJND-XX-2020'
code2 = 'FVNISJND-XY-2019'
print(f'code1: {code1.endswith("2020")}\ncode2: {code2.endswith("2020")}')

# %%
##
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
print(f'path1: {path1.startswith("you")}')
print(f'path2: {path2.startswith("you")}')

# %%
##
path1 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
path2 = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-deep-learning-engineer'
path3 = 'https://e-smartdata.teachable.com/p/sciezka-bi-analyst-data-analyst'
print(f"path1: {path1.find('scientist')}")
print(f"path2: {path2.find('scientist')}")
print(f"path3: {path3.find('scientist')}")

# %%
##
code1 = 'FVNISJND-20'
code2 = 'FVNISJND20'
print(f'code1: {code1.isalnum()}')
print(f'code2: {code2.isalnum()}')

# %%
##
text = 'Google Colab'
print(text.lower())

# %%
##
text = 'Google Colab'
print(text.upper())

# %%
##
text = '  Google Colab   '
print(text.strip())

# %%
##
code = 'FVNISJND-XX'
print(code.replace("-", " "))

# %%
##
text = '340-23-245-235'
print(text.replace('-', ''))

# %%
##
text = 'Open,High,Low,Close'
print(text.split(','))

# %%
##
text = """Python jest językiem ogólnego przeznaczenia.
Python jest popularny."""
# print(text.split('\n'))
print(text.splitlines())

# %%
##
num = 34
# print('0000' + str(num))
print(str(num).zfill(6))

# %%
##
url = 'https://e-smartdata.teachable.com/p/sciezka-data-scientist-machine-learning-engineer'
# print(url[36:].replace('-', ' '))
print(url.split('/')[-1].replace('-', ' '))
