# %%
##
import calendar as cal
from datetime import date as dt
import re
import string as st
from collections import Counter
import math
import random
import pickle
import json

# %%
##
s = cal.calendar(2020)

print(s)

# %%
##
s = cal.month(2020, 6)

print(s)

# %%
##
d_1 = dt(2020, 6, 1)
d_2 = dt(2020, 7, 18)

print(d_2 - d_1)

# %%
##
string = 'Python 3.8'

p = re.compile(pattern=r"\d").findall(string)

print(p)

# different solution

result = re.findall(pattern=r"\d", string=string)
print(result)

# %%
##
string = '!@#$%^&45wc'

res = re.findall(r"\w", string=string)

print(res)

# %%
##
raw_text = "Wyślij email na adres: info@template.com lub sales-info@template.it"

res = re.findall(r"[\w.-]+@[\w.-]+", raw_text)

print(res)

# %%
##
text = 'Programowanie w języku Python - od A do Z'

res = re.split(r"\s+", text)

print(res)

# %%
##
res = st.ascii_letters

print(res)

# %%
##
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']

res = Counter(items)

print(res)

# or
counter = Counter()
items = ['YES', 'NO', 'NO', 'YES', 'EMPTY', 'YES', 'NO']
for item in items:
    counter[item] += 1
print(counter)


# %%
##


def sigmoid(x):
    func = 1 / (1 + math.exp(-x))
    return func


# %%
##


random.seed(12)

items = ['python', 'java', 'sql', 'c++', 'c']

print(random.choice(items))

# %%
##


random.seed(15)

items = ['python', 'java', 'sql', 'c++', 'c']
random.shuffle(items)

print(items)

# %%
##
ids = ['001', '003', '011']

pickle.dump(ids, open('data.pickle', 'wb'))

# %%
##
stocks = {'PLW': 360.0, 'TEN': 320.0, 'CDR': 329.0}

print(json.dumps(stocks, sort_keys=True, indent=4))
