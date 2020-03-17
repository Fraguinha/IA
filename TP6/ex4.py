import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

data = np.loadtxt('regression.txt')

X = data[:, 0].reshape(-1, 1)
Y = data[:, 1].reshape(-1, 1)

clf = tree.DecisionTreeRegressor()
clf.fit(X, Y)

prediction = clf.predict([[11.5]])[0]

print("Prediction:", prediction)

plt.plot(X, Y, 'bo')
plt.plot(11.5, prediction, 'rx')
plt.show()
