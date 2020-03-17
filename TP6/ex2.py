import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

data = np.loadtxt('CTG.csv', delimiter=',')
X = data[:, 0:21]
Y = data[:, 21]

# Conjunto de teste
testX = X[:126]
testY = Y[:126]

# Conjunto de treino
trainX = X[126:]
trainY = Y[126:]

size = [100, 200, 500, 1000, 2000]
p = []
for i in size:
    tX = trainX[:i]
    tY = trainY[:i]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(tX, tY)
    yPredict = clf.predict(testX)

    c = 0
    for a, b in zip(yPredict, testY):
        if a == b:
            c += 1
    print(i)
    print(c / 126)
    p.append(c/126)

plt.plot(size, p)
plt.show()
