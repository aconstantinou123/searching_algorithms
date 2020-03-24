def recursive_search(a, i, x):
    n = len(a) - 1
    if i > n:
        return -1
    elif a[i] == x:
        return i
    else:
        return recursive_search(a, i + 1, x)