# %%
##
y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]


def accuracy(y_t, y_p):
    counter = 0
    for i, j in zip(y_t, y_p):
        if i == j:
            counter += 1
    return round(counter / len(y_t), 4)


print(accuracy(y_true, y_pred))

# %%
##
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]


def mae(y_true, y_pred):
    sum = 0
    # for i, j in zip(y_true, y_pred):
    #     sum += abs(j - i)
    for i in zip(y_true, y_pred):
        sum += abs(i[1] - i[0])
    return round(sum / len(y_pred), 3)


mae(y_true, y_pred)

# %%
##
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]


def mse(yt, yp):
    res = sum([pow(j - i, 2) for i, j in zip(yt, yp)])
    return round(res / len(yt), 3)


mse(y_true, y_pred)


# %%
##


def relu(x):
    return max(x, 0)


# %%
##
items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def flatten(lst):
    res = []
    for i in lst:
        for j in i:
            res.append(j)
    return res


flatten(items)


# or

def flatten_2(lst):
    res = []
    for item in lst:
        res.extend(item)
    return res


flatten_2(items)

# %%
##

items = [3, 4, 0, 2, 0, 5, 1, 6, 2]


def transfer_zeros(lst):
    res = []
    for item in lst:
        if item != 0:
            res.append(item)
    for item in lst:
        if item == 0:
            res.insert(len(res), item)
    return res


transfer_zeros(items)

# %%
##
x = [0, 3]
y = [4, 0]


def euclidean_distance(l_1, l_2):
    sum = 0
    for i, j in zip(l_1, l_2):
        sum += pow(j - i, 2)
    return pow(sum, 1 / 2)

    # return [pow(sum(pow(j - i, 2)), 1 / 2) for i, j in zip(l_1, l_2)]


euclidean_distance(x, y)


# %%
##


def identity(n):
    res = []
    count = 0
    for i in range(n):
        foo = list(0 for j in range(n))
        foo[count] += 1
        res.append(foo)
        count += 1
    return res


identity(5)

print('\n')


def identity_2(m):
    array = [[0] * m for i in range(m)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array


identity_2(6)


# %%
##


def fill_value(h, w, v):
    # return [[v] * w for i in range(h)]
    res = []
    for i in range(h):
        res.append([v for j in range(w)])
    return res


fill_value(5, 9, '*')


# %%
##


def trace(array):
    return sum([item[idx] for idx, item in enumerate(array)])


trace([[1]])
trace([[1, 2], [4, 2]])
trace([[3, 4, 5], [5, 2, 1], [5, 7, 2]])


# %%
##


def transpose(array):
    return [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]


transpose([[1, 2, 3], [4, 5, 6]])


# %%
##


def max_prob(array):
    res = []
    for i in array:
        for j in i:
            return max(j)


max_prob([[0.3, 0.4, 0.3], [[0.0, 0.1, 0.9]]])
