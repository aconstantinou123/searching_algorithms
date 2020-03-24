# O(n)
def linear_search(a, x):
    for i in a:
        if i == x:
            return i
    return -1