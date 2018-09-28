"""Utilities for implementing the algorithms."""


def enumerate_slice(lst, start, end=None):
    """Equivalent to enumerate(lst[start:end]), but does not make a copy of the
    slice.

    Complexity: O(end-start) time, O(1) space.
    """
    if end is None:
        end = len(lst)
    while start < end:
        yield start, lst[start]
        start += 1
