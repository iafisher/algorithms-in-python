"""Utilities for implementing the algorithms, including custom type annotations.
"""

from typing import Dict, Iterator, List, Optional, Tuple, Union


def iterate_slice(lst: list, start: int, end: Optional[int] = None) -> Iterator:
    """Equivalent to iter(lst[start:end]), but does not make a copy of the
    slice.

    Complexity: O(end-start) time, O(1) space.
    """
    if end is None:
        end = len(lst)
    while start < end:
        yield lst[start]
        start += 1


# Custom type annotations.
Number = Union[int, float]
AdjacencyList = Dict[str, List[str]]
WeightedAdjacencyList = Dict[str, List[Tuple[str, Number]]]
Point = Tuple[Number, Number]
