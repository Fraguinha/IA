from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np
import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


train = np.loadtxt('espiral_train.csv', delimiter=',')
test = np.loadtxt('espiral_test.csv', delimiter=',')

trainX = train[:, :2]
trainY = train[:, 2]
testX = test[:, :2]
testY = test[:, 2]

k = int(input("k: "))

y_pred = []
for x, y in testX:

    dist = []
    for (xi, yi), l in zip(trainX, trainY):
        dist.append((distance((x, y), (xi, yi)), l))

    dist = sorted(dist)
    kNN = dist[:k]

    lbl = {}
    for el in kNN:
        d, l = el
        if l in lbl:
            lbl[l] = lbl[l] + 1
        else:
            lbl[l] = 1

    max_v = -1
    max_l = -1
    for key in lbl.keys():
        if lbl[key] > max_v:
            max_v = lbl[key]
            max_l = key
    y_pred.append(max_l)

y_pred2 = []
for x, y in trainX:

    dist = []
    for (xi, yi), l in zip(trainX, trainY):
        dist.append((distance((x, y), (xi, yi)), l))

    dist = sorted(dist)
    kNN = dist[:k]

    lbl = {}
    for el in kNN:
        d, l = el
        if l in lbl:
            lbl[l] = lbl[l] + 1
        else:
            lbl[l] = 1

    max_v = -1
    max_l = -1
    for key in lbl.keys():
        if lbl[key] > max_v:
            max_v = lbl[key]
            max_l = key
    y_pred2.append(max_l)


print("Número de erros em %d pontos de treino: %d"
      % (testX.shape[0], (testY != y_pred).sum()))

print("Número de erros em %d pontos de treino: %d"
      % (trainX.shape[0], (trainY != y_pred2).sum()))
