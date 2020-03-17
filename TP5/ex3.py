# UBI, AI, 2019
# ----------------------------------
from bayesian.bbn import build_bbn
import sys
sys.path.append('bayesian')


def f_chuva(chuva):
    if chuva:
        return 0.2
    else:
        return 0.8


def f_aspersor(chuva, aspersor):
    if chuva and aspersor:
        return 0.01
    elif chuva and not aspersor:
        return 0.99
    elif not chuva and aspersor:
        return 0.4
    elif not chuva and not aspersor:
        return 0.6


def f_relva_molhada(chuva, aspersor, relva_molhada):
    if relva_molhada:
        if chuva and aspersor:
            return 0.99
        elif not chuva and aspersor:
            return 0.9
        elif chuva and not aspersor:
            return 0.8
        elif not chuva and not aspersor:
            return 0
    else:
        if chuva and aspersor:
            return 0.01
        elif not chuva and aspersor:
            return 0.1
        elif chuva and not aspersor:
            return 0.2
        elif not chuva and not aspersor:
            return 1


if __name__ == '__main__':
    g = build_bbn(
        f_chuva,
        f_aspersor,
        f_relva_molhada,
        domains=dict(
            chuva=[True, False],
            aspersor=[True, False],
            relva_molhada=[True, False]))
