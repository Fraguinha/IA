import os

d = {}


def insert():
    os.system("clear")
    uc = input("Nome UC: ")
    nota = input("Nota: ")
    d[uc] = nota
    os.system("clear")
    input("UC adicionada")


def change():
    os.system("clear")
    uc = input("Nome UC: ")
    if uc in d:
        nota = input("Nota: ")
        d[uc] = nota
        os.system("clear")
        input("Nota UC alterada")
    else:
        os.system("clear")
        input("UC nao existe")


def show():
    os.system("clear")
    for i in d.items():
        print(i)
    input()


def calculate():
    os.system("clear")
    sum = 0
    num = 0
    for nota in d.values():
        sum += int(nota)
        num += 1
    avg = sum / num
    input("Media:", str(avg))


end = False
while not end:
    os.system("clear")
    print("1: Inserir UC/nota")
    print("2: Alterar nota de UC")
    print("3: Mostrar todas as notas")
    print("4: Calcular media das UC")
    print()
    print("0: Sair")
    print()
    opt = input("Opcao: ")

    if opt == "0":
        end = True
    elif opt == "1":
        insert()
    elif opt == "2":
        change()
    elif opt == "3":
        show()
    elif opt == "4":
        calculate()
    else:
        os.system("clear")
        print("Opcao invalida")
