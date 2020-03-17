def ler():
    return input()


def gravar(s, filename):
    fp = open(filename, "w")
    fp.write(s)
    fp.close()


def contaVogais(s):
    c = 0
    for l in s:
        if l in ["a", "e", "i", "o", "u"]:
            c += 1
    return c


str = input("frase: ")
print(contaVogais(str))
