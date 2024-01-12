def fakultaet(n):
    if n == 1:
        return 1
    return n * fakultaet(n - 1)

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(3))

def joe(n):
    if n == 1:
        return 1
    a=
    return n + sum_n(n - 1)

print(sum_n(3))

"""
# 1 4 x fak(3) 4 x 6 = 24
# 2 3 x fak(2) 3 x 2 = 6
# 3 2 x fak(1) -> 2 x 1 = 2
# 4 return 1 -> = 1
"""