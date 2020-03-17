import numpy as np

A = []
B = []

print("A:")
for i in range(4):
    i = int(input())
    A.append(i)

print("B:")
for i in range(4):
    i = int(input())
    B.append(i)

A = np.array(A)
B = np.array(B)

A = A.reshape(2, 2)
B = B.reshape(2, 2)

print("elementwise multiplication:")
print(A * B)

print("matrix multiplication:")
print(np.matmul(A, B))

print("matrix difference:")
print(A - B)

print("matrix function application:")
print(np.abs(np.log(A)))

A = A.reshape(-1)
print("Argmax A:")
print(A[np.argmax(A)])

B = B.reshape(-1)
print("Argmin B:")
print(B[np.argmin(B)])
