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
# y_true = [0, 0, 1, 1, 0, 1, 0]
# y_pred = [0, 0, 1, 0, 0, 1, 0]


def mea(y_true, y_pred):
    sum = 0
    for i, j in zip(y_true, y_pred):
        sum += abs(y_pred[j] - y_true[i])
    return sum / len(y_pred)


mea(y_true, y_pred)
