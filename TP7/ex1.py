import numpy as np

data = np.loadtxt('size_price.csv', delimiter=',')

n = len(data[:, 0])

xiyi = 0
xi = 0
yi = 0
xi2 = 0
for s, p in data:
    xi += s
    yi += p
    xiyi += (s * p)
    xi2 += s**2

w1 = (n * xiyi - xi * yi) / (n * xi2 - xi ** 2)
w0 = (yi - w1 * xi) / n


def predict(input_size):
    return w1 * input_size + w0


while True:
    input_size = int(input("Tamanho da casa: "))
    if (input_size < 0):
        break
    print(predict(input_size))

ee = 0
for s, p in data:
    ee += (p - predict(s)) ** 2

print("Erro Empírico:", ee)
