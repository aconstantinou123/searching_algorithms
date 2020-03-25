from math import floor

def recursive_binary_search(a, p, r, x):
    if p > r:
        return - 1
    else:
        q = floor((p + r) / 2)
        if a[q] == x:
            return q
        elif a[q] > x:
            return recursive_binary_search(a, p, q - 1, x)
        else:
            return recursive_binary_search(a, q + 1, r, x)