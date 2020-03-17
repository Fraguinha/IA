import matplotlib.pyplot as plt

pp = [0.01, 0.2, 0.5, 0.8, 0.99]
pc13 = [0.020, 0.307, 0.602, 0.827, 0.990]
pc22 = [0.991, 0.866, 0.795, 0.861, 0.991]

plt.plot(pp, pc13)
plt.plot(pp, pc22)
plt.show()
