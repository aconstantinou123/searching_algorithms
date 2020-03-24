from math import floor

def binary_search(x, a):
    p = 0
    r = len(a) -1
    while p <= r:
        q = floor((p + r) / 2)
        if a[q] > x:
            r = q - 1
        elif a[q] < x:
            p = q + 1
        else:
            return q
    return -1