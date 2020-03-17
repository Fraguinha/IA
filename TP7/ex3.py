from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np

train = np.loadtxt('espiral_train.csv', delimiter=',')
test = np.loadtxt('espiral_test.csv', delimiter=',')

trainX = train[:, :2]
trainY = train[:, 2]
testX = test[:, :2]
testY = test[:, 2]

gnb = GaussianNB()

y_pred = gnb.fit(trainX, trainY).predict(testX)
y_pred2 = gnb.fit(trainX, trainY).predict(trainX)
print("Número de erros em %d pontos de treino: %d"
      % (testX.shape[0], (testY != y_pred).sum()))

print("Número de erros em %d pontos de treino: %d"
      % (trainX.shape[0], (trainY != y_pred2).sum()))
