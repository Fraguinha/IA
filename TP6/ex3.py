import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import ShuffleSplit

data = np.loadtxt('CTG.csv', delimiter=',')
X = data[:, 0:21]
Y = data[:, 21]

ss = ShuffleSplit(n_splits=10, random_state=None, test_size=126,
                  train_size=len(data[:, 0])-126)


num_correct = []
for train_index, test_index in ss.split(X):
    trainX = []
    trainY = []
    testX = []
    testY = []
    for i in train_index:
        trainX.append(X[i])
        trainY.append(Y[i])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(trainX, trainY)

    for i in test_index:
        testX.append(X[i])
        testY.append(Y[i])

    prediction = clf.predict(testX)
    c = 0
    for p, y in zip(prediction, testY):
        if p == y:
            c += 1
    num_correct.append(c / len(testY))

plt.plot(num_correct)
plt.show()
