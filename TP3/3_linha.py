# coding: utf8
import copy
import random
import time

# ------------------------------------------------------------------


def mostra_tabuleiro(T):
    for i in range(len(T)):
        if T[i] == 1:
            print("X", end=" ")
        elif T[i] == 0:
            print(".", end=" ")
        else:
            print("O", end=" ")

        if i % 4 == 3:
            print()


# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T):
    a = []
    for i in range(len(T)):
        if T[i] == 0 and (i >= 8 or T[i+4] == 1 or T[i+4] == -1):
            a.append(i)
    return a


# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T, a, jog):
    aux = copy.copy(T)
    if jog == "MAX" or jog == "HUMAN" or jog == "RAND":
        aux[a] = 1
    else:
        aux[a] = -1
    return aux


# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador


def utilidade(T):
    # testa as linhas
    for i in (0, 1, 4, 5, 8, 9):
        sum = T[i] + T[i+1] + T[i+2]
        if sum == 3:
            return 1
        elif sum == -3:
            return - 1
    # testa as colunas
    for i in (0, 1, 2, 3):
        sum = T[i] + T[i + 4] + T[i + 8]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1

    sum_d1 = T[0] + T[5] + T[10]
    sum_d2 = T[1] + T[6] + T[11]
    sum_d3 = T[2] + T[5] + T[8]
    sum_d4 = T[3] + T[6] + T[9]
    if sum_d1 == 3 or sum_d2 == 3 or sum_d3 == 3 or sum_d4 == 3:
        return 1
    if sum_d1 == -3 or sum_d2 == -3 or sum_d3 == -3 or sum_d4 == -3:
        return -1
    # não é nodo folha ou dá empate
    return 0


# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
def estado_terminal(T):
    if acoes(T) == [] or utilidade(T) == 1 or utilidade(T) == -1:
        return True
    return False


def alfabeta(T, alfa, beta, jog):
    if estado_terminal(T):
        return utilidade(T), -1, -1
    if jog:
        v = -10
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, "MAX"), alfa, beta, False)
            if v1 > v:  # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            alfa = max(alfa, v)
            if beta <= alfa:
                break
        return v, ba, resultado(T, ba, "MAX")
    else:
        v = 10
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, "MIN"), alfa, beta, True)
            if v1 < v:  # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            beta = min(beta, v)
            if beta <= alfa:
                break
        return v, ba, resultado(T, ba, "MIN")
    # ------------------------------------------------------------------


def joga_max(T):
    v, a, e = alfabeta(T, -10, 10, True)
    print("MAX joga para ", a)
    return e


# ------------------------------------------------------------------


def joga_min(T):
    v, a, e = alfabeta(T, -10, 10, False)
    #print("MIN joga para ", a)
    return e


# ------------------------------------------------------------------


def joga_human(T):
    x = -1
    while x not in acoes(T):
        x = int(input("Introduza uma jogada: "))
    print("HUMAN joga para ", x)
    return resultado(T, x, "HUMAN")


# ------------------------------------------------------------------
# jogador aleatório
3


def joga_rand(T):
    x = random.choice(acoes(T))
    #print("RAND joga para ", x)
    return resultado(T, x, "RAND")


# ------------------------------------------------------------------


def jogo(p1, p2):
    # cria tabuleiro vazio
    T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # mostra_tabuleiro(T)
    while acoes(T) != [] and not estado_terminal(T):
        T = p1(T)
        # mostra_tabuleiro(T)
        if acoes(T) != [] and not estado_terminal(T):
            T = p2(T)
            # mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        #print("Venceu o jog1")
        return 1
    elif utilidade(T) == -1:
        #print("Venceu o jog2")
        return -1
    else:
        # print("Empate")
        return 0


# ------------------------------------------------------------------
# main
# deve ganhar sempre o max:
# jogo(joga_max, joga_min)
# deve ganhar sempre o max:
RAND = 0
MIN = 0
empate = 0
t = time.time()
for i in range(1000):
    x = jogo(joga_rand, joga_min)
    if x == 1:
        RAND += 1
    elif x == -1:
        MIN += 1
    else:
        empate += 1
print("RAND: " + str(RAND))
print("MIN: " + str(MIN))
print("Empate: " + str(empate))
print("Tempo: " + str(time.time()-t))

#jogo(joga_human, joga_min)
# jogo(joga_human, joga_rand)
