"""Brute-force and exhaustive search algorithms solve a problem by generating
all possible solutions until the correct one is found. Brute-force algorithms
are often simple to design and implement, but computationally expensive.

Backtracking, branch-and-bound and approximation can be used to improve the
performance of brute-force algorithms for problems with no known better
algorithms.
"""

def linear_search(lst: list, x) -> int:
    """Return the index of the first element of `lst` equal to `x`, or -1 if no
    elements of `lst` are equal to `x`.

    Design idea: Scan the list from start to finish.

    Complexity: O(n) time, O(1) space.
    """
    for i, y in enumerate(lst):
        if x == y:
            return i
    return -1
