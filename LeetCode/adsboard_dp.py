import math

abs = [(5, 5), (6, 6), (12, 5), (13, 1)]


def best_value(idx):
    if idx == 0:
        return 0
    pos, val = abs[idx - 1]
    if idx > 0:
        prev = e(idx - 1)
        return max(best_value(idx - 1), best_value(prev) + val)


def e(i):
    ori = i
    while i - 1 > 0:
        if math.fabs(abs[i - 1][0] - abs[ori][0]) > 5:
            print(abs[i - 1][0], abs[ori][0])
            return i
        i -= 1
    return 0


result = []
i = 0

print(best_value(len(abs)), result)
print(best_value(3))
print(best_value(2))
print(best_value(1))
print(best_value(0))
