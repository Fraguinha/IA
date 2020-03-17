# UBI, AI, 2019
# ----------------------------------
from bayesian.bbn import build_bbn
import sys
sys.path.append('bayesian')


def f_prize_door(prize_door):
    return 0.33333333


def f_guest_door(guest_door):
    return 0.33333333


def f_monty_door(prize_door, guest_door, monty_door):
    if monty_door == guest_door or prize_door == monty_door:
        return 0
    elif prize_door == guest_door:
        return 0.5
    else:
        return 1


if __name__ == '__main__':
    g = build_bbn(
        f_prize_door,
        f_guest_door,
        f_monty_door,
        domains=dict(
            prize_door=['A', 'B', 'C'],
            guest_door=['A', 'B', 'C'],
            monty_door=['A', 'B', 'C']))
