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
