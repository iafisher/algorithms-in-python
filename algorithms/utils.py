"""Utilities for implementing the algorithms."""


def iterate_slice(lst, start, end=None):
    """Equivalent to iter(lst[start:end]), but does not make a copy of the
    slice.

    Complexity: O(end-start) time, O(1) space.
    """
    if end is None:
        end = len(lst)
    while start < end:
        yield lst[start]
        start += 1
