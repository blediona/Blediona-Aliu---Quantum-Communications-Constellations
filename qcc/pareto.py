import numpy as np


def dominates(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    return bool(np.all(a <= b) and np.any(a < b))


def nondominated_naive(F):
    F = np.asarray(F)
    keep = []
    for i in range(len(F)):
        if not any(dominates(F[j], F[i]) for j in range(len(F)) if j != i):
            keep.append(i)
    return np.array(keep, dtype=int)