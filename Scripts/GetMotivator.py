import random as rn


def get_motivator():
    f = open('TextFiles/Motivators.txt', 'r', encoding="utf-8")
    lines = f.read().split("\n")
    return rn.choice(lines)
    f.close()
