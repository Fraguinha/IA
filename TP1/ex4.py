def lerLista():
    l = []
    while True:
        i = int(input())
        if i >= 0:
            l.append(i)
        else:
            return l


def both(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    r = list(l1.intersection(l2))
    return r


print("L1:")
l1 = lerLista()
print("L2:")
l2 = lerLista()

print(both(l1, l2))
