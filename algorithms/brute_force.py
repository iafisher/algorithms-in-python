"""Brute-force and exhaustive search algorithms solve a problem by generating
all possible solutions until the correct one is found. Brute-force algorithms
are often simple to design and implement, but computationally expensive.

Backtracking, branch-and-bound and approximation can be used to improve the
performance of brute-force algorithms for problems with no known better
algorithms.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: September 2018
"""

def linear_search(lst: list, x) -> int:
    """Return the index of the first element of `lst` equal to `x`, or -1 if no
    elements of `lst` are equal to `x`.

    Design idea: Scan the list from start to finish.

    Complexity: O(n) time, O(1) space.

    For an improvement on linear search for sorted lists, see the binary search
    function in the decrease_and_conquer module.
    """
    for i, y in enumerate(lst):
        if x == y:
            return i
    return -1


def bubble_sort(lst: list) -> list:
    """Sort a list in ascending order.

    Design idea: Swap adjacent out-of-order elements until the list is sorted.

    Complexity: O(n^2) time, O(1) space. Stable and in-place.

    See quicksort, merge sort and heapsort for sorting algorithms with a better
    time complexity.
    """
    # The first iteration will bring the largest element to the end, the second
    # iteration will bring the second largest element to the end - 1, and so on,
    # so we need no more than n iterations to put every element in the proper
    # place.
    for _ in range(len(lst)):
        swapped = False
        for i in range(1, len(lst)):
            # If you changed this comparison to >=, the algorithm would still
            # be correct but the sort would no longer be stable.
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                swapped = True
        # If no swaps occurred, the list is sorted and we can exit early.
        if not swapped:
            break
    return lst


def selection_sort(lst: list) -> list:
    """Sort a list in ascending order.

    Design idea: Find the smallest element in the list and swap it to the front.
    Find the second smallest element and swap it to the second position.
    Continue until you reach the end, at which point the list will be sorted.

    Complexity: O(n^2) time, O(1) space. Stable and in-place.
    
    See quicksort, merge sort and heapsort for sorting algorithms with a better
    time complexity.
    """
    for i in range(len(lst)):
        minimum = lst[i]
        minimum_index = i
        # Find the minimum element in the rest of the list.
        for j in range(i+1, len(lst)):
            # As in bubble sort, this must be < and not <= for the sort to be
            # stable.
            if lst[j] < minimum:
                minimum = lst[j]
                minimum_index = j
        # Swap the i'th element with the minimum in the rest of the list. The
        # first i elements of the list will not change after this iteration.
        lst[i], lst[minimum_index] = lst[minimum_index], lst[i]
    return lst


def find_substring(text: str, pattern: str) -> int:
    """Return the index of the first character of the first occurrence of
    `pattern` as a subsequence of `text`. If `pattern` never occurs, return -1.

    Design idea: For each character of the text that matches the first character
    of the pattern, check if the subsequent characters also match.

    Complexity: O(n*m) time, O(1) space.
    """
    if len(pattern) == 0:
        return 0

    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            elif j == len(pattern) - 1:
                return i
    return -1
