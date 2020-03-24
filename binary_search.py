from math import floor

def binary_search(x, a):
    p = 0
    r = len(a) -1
    while p <= r:
        q = floor((p + r) / 2)
        if a[q] == x:
            return q
        elif a[q] > x:
            r = q - 1
        else:
            p = q + 1
    return -1