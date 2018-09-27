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


def selection_sort(lst: list) -> list:
    """Sort a list in ascending order.

    Design idea: Find the smallest element in the list and swap it to the front.
    Find the second smallest element and swap it to the second position.
    Continue until you reach the end, at which point the list will be sorted.

    Complexity: O(n^2) time, O(1) space. Stable and in-place.
    """
    for i in range(len(lst)):
        minimum = lst[i]
        minimum_index = i
        # Find the minimum element in the rest of the list.
        for j in range(i+1, len(lst)):
            # If you changed this comparison to <=, the algorithm would still
            # be correct but the sort would no longer be stable.
            if lst[j] < minimum:
                minimum = lst[j]
                minimum_index = j
        # Swap the i'th element with the minimum in the rest of the list. The
        # first i elements of the list will not change after this iteration.
        lst[i], lst[minimum_index] = lst[minimum_index], lst[i]
    return lst
