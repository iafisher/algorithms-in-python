def merge_sort(lst: list) -> list:
    """Sort a list in ascending order. The original list is mutated and
    returned. The sort is stable.

    Design idea: Split the list in half, sort each half recursively, and then
    merge the two halves with a linear-time merging algorithm.

    Complexity: O(n log n) time, O(n) space.
    """
    if len(lst) > 1:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right, lst)
    else:
        return lst


def merge(lst1: list, lst2: list, into: list) -> list:
    """Merge two sorted lists into a single sorted list.

    Complexity: O(n) time, O(1) space.
    """
    i1 = 0
    i2 = 0
    i3 = 0
    while i1 < len(lst1) and i2 < len(lst2):
        # The comparison must be <= for the merge (and hence the sort) to be
        # stable.
        if lst1[i1] <= lst2[i2]:
            into[i3] = lst1[i1]
            i1 += 1
        else:
            into[i3] = lst2[i2]
            i2 += 1
        i3 += 1
    # Take care of any remaining elements for lists of unequal lengths. Only
    # one of these loops will execute on any given merge.
    for i in range(i1, len(lst1)):
        into[i3] = lst1[i]
        i3 += 1
    for i in range(i2, len(lst2)):
        into[i3] = lst2[i]
        i3 += 1
    return into
