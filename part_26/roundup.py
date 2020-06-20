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
