from sklearn import svm
import numpy as np

train = np.loadtxt('espiral_train.csv', delimiter=',')
test = np.loadtxt('espiral_test.csv', delimiter=',')

trainX = train[:, 0:2]
trainY = train[:, 2]
testX = test[:, 0:2]
testY = test[:, 2]

clf = svm.SVC(C=1000, gamma='auto')
clf.fit(trainX, trainY)

prediction = clf.predict(testX)
prediction2 = clf.predict(trainX)

error = 0
for p, l in zip(prediction, testY):
    if p != l:
        error += 1

error2 = 0
for p, l in zip(prediction2, trainY):
    if p != l:
        error2 += 1


print("Erro Teste:", error / len(testY))
print("Erro Treino:", error2/len(trainY))
