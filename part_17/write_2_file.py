# %%
##
even_numb = list(range(2, 20))[::2]
# for i in range(1, 20):
#     if i % 2 == 0:
#         even_numb.append(i)

with open('part_17\\num.txt', 'w') as f:
    for num in even_numb:
        f.write(str(num) + '\n')
# %%
##
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('part_17\\stocks.json', 'w') as jf:
    json.dump(stocks, jf, indent=4)

# %%
##
import csv

headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('part_17\\users.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(headers)
    for j in users:
        writer.writerow(j)

# %% or
##
headers = ['user_id', 'amount']
users = [['001', '1400'], ['004', '1300'], ['007', '900']]

with open('part_17\\users_1.csv', 'w') as file:
    file.write(','.join(headers) + '\n')
    for user in users:
        file.write(','.join(user) + '\n')
