"""A decrease-and-conquer algorithm solves a problem by continually reducing it
into a smaller version of the same problem. For example, a^n can be computed by
first computing a^(n-1) and then multiplying by a. Decrease-and-conquer
algorithms are naturally expressed with recursion, although iterative
implementations may be more efficient.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: September 2018
"""


def binary_search(lst: list, x) -> int:
    """Return the index of the first element of the sorted list `lst` equal to
    `x`, or -1 if no elements of `lst` are equal to `x`.

    Design idea: Compare the given element with the midpoint element of the
    list. If the element is less than the midpoint, then recursively search the
    left half. If the element is greater, then recursively search the right
    half.

    Complexity: O(log n) time, O(1) space.
    """
    # `lo` is the first index of the list still under consideration, and `hi` is
    # one past the last index under consideration. `hi - lo` will always be the
    # number of elements under consideration.
    lo = 0
    hi = len(lst)
    while lo < hi:
        mid = (lo + hi) // 2
        # Use the comparison with the midpoint to rule out half the list.
        if x == lst[mid]:
            return mid
        elif x < lst[mid]:
            hi = mid
        else:
            lo = mid + 1
    return -1


def insertion_sort(lst: list) -> list:
    """Sort a list in ascending order. The original list is mutated and
    returned. The sort is stable.

    Design idea: Iterate over the list. After i iterations, the first i elements
    of the list should be sorted. Insert the i+1'th element in the appropriate
    spot in the sorted sublist. Note that this idea differs from selection sort
    in that the first i elements are sorted, but not necessarily in their final
    order.

    Complexity: O(n^2) time, O(1) space. Stable and in-place.
    """
    for i in range(1, len(lst)):
        v = lst[i]
        j = i - 1
        # Keep shifting elements over until we hit an element equal to or less
        # than `v`.
        while j >= 0 and lst[j] > v:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = v
    return lst
