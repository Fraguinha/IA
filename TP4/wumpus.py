import random
import time


def generate():
    s = [False, False, False]
    valid = False
    while not valid:
        for i in range(3):
            if random.random() <= 0.2:
                s[i] = True
            else:
                s[i] = False
        if ((s[0] or s[1]) and (s[1] or s[2])):
            valid = True
    return s[0], s[1], s[2]


c0 = 0
c1 = 0
c2 = 0
t = time.time()
for i in range(10000):
    s0, s1, s2 = generate()
    if s0:
        c0 += 1
    if s1:
        c1 += 1
    if s2:
        c2 += 1

print("Probabilidade de poço em (1,3):", c0 / 10000)
print("Probabilidade de poço em (2,2):", c1 / 10000)
print("Probabilidade de poço em (3,1):", c2 / 10000)
print("Tempo: " + str(time.time()-t))
