from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[str]):
    # TODO - you fill in here.
    for i in range(len(A)):
        while perm[i] != i:  # while value in permuatation array not equal to index
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]

    return A


print(apply_permutation([2, 0, 1, 3], ["a", "b", "c", "d"]))
