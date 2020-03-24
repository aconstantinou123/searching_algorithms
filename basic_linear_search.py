# O(n)
def linear_search(x, a):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1