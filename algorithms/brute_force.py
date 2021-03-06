"""Brute-force algorithms solve a problem by generating all possible solutions
until the correct one is found. They are often simple to design and implement,
but computationally expensive.

Backtracking, branch-and-bound and approximation can be used to improve the
performance of brute-force algorithms for problems with no known better
algorithms.

Exhaustive search algorithms iterate over every element of a collection to find
an element with some particular property. Examples are linear search, and depth-
first and breadth-first traversals of graphs. Such algorithms can sometimes be
improved to exploit particular properties of the collection. For example, sorted
lists can be searched in O(log n) time with binary search instead of O(n) time
with linear search.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: October 2018
"""

from typing import Any, Dict, FrozenSet, Iterator, List, Optional, Set, Tuple

from .decrease_and_conquer import subsets
from .utils import AdjacencyList, Point, WeightedAdjacencyList, iterate_slice


def linear_search(lst: list, x: Any) -> int:
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
    """Sort a list in ascending order. The original list is mutated and
    returned. The sort is stable.

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
    """Sort a list in ascending order. The original list is mutated and
    returned. The sort is not stable.

    Design idea: Find the smallest element in the list and swap it to the front.
    Find the second smallest element and swap it to the second position.
    Continue until you reach the end, at which point the list will be sorted.

    Complexity: O(n^2) time, O(1) space.

    See quicksort, merge sort and heapsort for sorting algorithms with a better
    time complexity.
    """
    for i in range(len(lst)):
        minimum = lst[i]
        minimum_index = i
        # Find the minimum element in the rest of the list.
        for j in range(i+1, len(lst)):
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


def depth_first_search(graph: AdjacencyList) -> Iterator[str]:
    """Yield every vertex in the graph (represented as an adjacency list) in
    depth-first order, i.e. starting at an arbitrary root and exploring as far
    as possible down each branch before backtracking.

    Design idea: We will make use of a recursive helper function that performs
    the DFS traversal of a connected subgraph rooted at a particular vertex.
    This function works by iterating over the vertex's neighbors and recursively
    traversing them. We will also need a dictionary to keep track of which
    vertices have been visited already, so that cycles in the graph will not
    cause the function to recurse infinitely.

    Complexity: O(|V| + |E|) time, O(|V|) space.
    """
    visited = set()
    for source in graph:
        if source not in visited:
            yield from depth_first_search_helper(graph, source, visited)


def depth_first_search_helper(
        graph: AdjacencyList, source: str, visited: Set[str]
    ) -> Iterator[str]:
    """Yield every vertex in the graph in depth-first order connected to the
    given vertex. `visited` should be a set of vertices that have already been
    visited.
    """
    yield source
    visited.add(source)
    for neighbor in graph[source]:
        if neighbor not in visited:
            yield from depth_first_search_helper(graph, neighbor, visited)


def breadth_first_search(graph: AdjacencyList) -> Iterator[str]:
    """Yield every vertex in the graph (represented as an adjacency list) in
    breadth-first order, i.e. starting at an arbitrary root and visiting each of
    its neighbors before visiting the neighbors of the root's first neighbors,
    and so on.

    Design idea: Similar to depth-first search, we will use a helper function
    to visit all the vertices of a connected subgraph.

    Complexity: O(|V| + |E|) time, O(|V|) space.
    """
    visited = set()
    for source in graph:
        if source not in visited:
            yield from breadth_first_search_helper(graph, source, visited)


def breadth_first_search_helper(
        graph: AdjacencyList, source: str, visited: Set[str]
    ) -> Iterator[str]:
    """Yield every vertex in the graph in breadth-first order connected to the
    given vertex. `visited` should be a set of vertices that have already been
    visited.
    """
    yield source
    visited.add(source)
    queue = [source]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                yield neighbor
                visited.add(neighbor)
                queue.append(neighbor)


def detect_cycle(graph: AdjacencyList) -> bool:
    """Return True if the graph contains a cycle.

    Design idea: Traverse the graph depth-first (breadth-first also works). If
    you ever reach a neighbor that has already been visited, you have found a
    cycle.

    Complexity: O(|V| + |E|) time, O(|V|) space.
    """
    # TODO: Actually the algorithm has to be different for directed and undirected
    # graphs, I think.
    visited = set()
    for source in graph:
        if source not in visited:
            if detect_cycle_helper(graph, source, visited):
                return True
    return False


def detect_cycle_helper(
        graph: AdjacencyList, source: str, visited: Set[str]
    ) -> bool:
    """Return True if the component of the graph connected to the given vertex
    contains a cycle. `visited` should be a set of vertices that have already
    been visited.
    """
    visited.add(source)
    stack = [source]
    while stack:
        vertex = stack.pop()
        for neighbor in graph[source]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(visited)
            else:
                if neighbor in stack:
                    return True
    return False


def closest_pair(points: List[Point]) -> Optional[Tuple[Point , Point]]:
    """Given a list of two-dimensional points, return the two closest distinct
    points. If the list is empty or has only one point, None is returned. If
    there is more than one closest pair, the one whose first point appears first
    in the list is returned. The first point in the returned pair always appears
    before the second point in the list.

    Design idea: Calculate the distance between every pair of points.

    Complexity: O(n^2) time, O(1) space.
    """
    closest_distance = None
    closest_pair = None
    for i, p1 in enumerate(points):
        for p2 in iterate_slice(points, i+1):
            # Note that for comparison purposes we do not need to compute the
            # square root to get the actual distance.
            distance = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_pair = (p1, p2)
    return closest_pair


def convex_hull(points: List[Point]) -> Set[Point]:
    """Return the set of points comprising the convex hull of the given points.
    The convex hull is the smallest convex (i.e., the perimeter has no
    indentations) set that encloses all the points.

    Design idea: The brute-force algorithm exploits the fact that any two points
    p1 and p2 are part of the convex hull iff all other points lie on the same
    side of the line through p1 and p2. This test can be repeated for every pair
    of points to find the convex hull.

    Complexity: O(n^3) time, O(1) space.
    """
    if len(points) < 3:
        return set(points)

    convex_hull = set()
    for i, p1 in enumerate(points):
        for p2 in iterate_slice(points, i+1):
            sign = None
            # The equation ax+by = c divides the plane into two half-planes:
            # one containing points for which ax+by > c and the other containing
            # points for which ax+by < c.
            a = p2[1] - p1[1]
            b = p1[0] - p2[0]
            c = p1[0]*p2[1] - p1[1]*p2[0]
            for p3 in points:
                if p3 == p1 or p3 == p2:
                    continue
                side = a*p3[0] + b*p3[1] - c
                if not sign:
                    sign = side
                elif not (
                    (side < 0 and sign < 0) or (side == 0 and sign == 0)
                    or (side > 0 and sign > 0)
                ):
                    break
            else:
                # The else case is run only when the loop exits normally and not
                # through a break statement.
                if side == 0:
                    # In the case that all of the points lie on the same line,
                    # the convex hull is just the endpoints of the line.
                    return find_endpoints(points)
                else:
                    convex_hull.add(p1)
                    convex_hull.add(p2)
    return convex_hull


def find_endpoints(points: List[Point]) -> Set[Point]:
    """Given a non-empty list of two-dimensional points on the same line, return
    the endpoints of the line.
    """
    max_x = points[0][0]
    max_x_point = points[0]
    min_x = points[0][0]
    min_x_point = points[0]
    for p in iterate_slice(points, 1):
        if p[0] > max_x:
            max_x_point = p
            max_x = p[0]
        elif p[0] < min_x:
            min_x_point = p
            min_x = p[0]
    return {max_x_point, min_x_point}


def traveling_salesman(graph: WeightedAdjacencyList) -> Optional[Tuple[str]]:
    """Given a graph with weighted edges, return the Hamiltonian circuit with
    the lowest sum of edge weights, or None if no Hamiltonian circuits exist.
    A Hamiltonian circuit is a path that visits each vertex of the graph exactly
    once before returning to the starting vertex.

    Design idea: Enumerate all permutations of the graph's vertices, check if
    each permutation represents a Hamiltonian circuit, and keep track of the
    most optimal one seen so far.

    Complexity: O((|V| + |E|) * |V|!) time, O(|V|^2) space (on account of
    `permutations()`).
    """
    best_path = None
    best_path_cost = None
    for path in permutations(list(graph.keys())):
        cost = hamiltonian_circuit_cost(graph, path)  # type: ignore
        if cost is not None:
            if best_path is None or cost < best_path_cost:
                best_path = path
                best_path_cost = cost
    return best_path  # type: ignore


def permutations(items: list) -> Iterator[tuple]:
    """Enumerate the permutations of `items` in lexicographic order.

    Complexity: O(n!) time, O(n^2) space.

    TODO: Better space complexity, and accept arbitrary iterators.
    """
    if len(items) == 1:
        yield (items[0],)
    else:
        for i, x in enumerate(items):
            for p in permutations(items[:i] + items[i+1:]):
                yield (x,) + p


def hamiltonian_circuit_cost(
        graph: WeightedAdjacencyList, path: List[str]
    ) -> Optional[float]:
    """If `path` represents a Hamiltonian circuit in `graph`, return the path's
    total cost (the sum of all the edge weights). If `path` is not a Hamiltonian
    circuit, return None.

    Complexity: O(|V| + |E|) time, O(|V|) space.
    """
    if not path:
        return 0 if not graph else None

    if len(set(path)) != len(path):
        return None

    cost = 0.0
    for i in range(len(path)):
        for vertex, weight in graph[path[i-1]]:
            if vertex == path[i]:
                cost += weight
                break
        else:
            return None
    return cost


def knapsack(
        items: Set[Tuple[float, float]], max_weight: float
    ) -> FrozenSet[Tuple[float, float]]:
    """Given a set of (value, weight) pairs and a maximum weight, return the
    most valuable subset of items whose total weight does not exceed the
    maximum weight.

    Design idea: Enumerate all subsets of the items and pick the one with the
    highest value that doesn't exceed the maximum weight.

    Complexity: O(2^n) time, O(n) space.
    """
    max_value = 0
    max_value_set: FrozenSet[Tuple[float, float]] = frozenset()
    for ss in subsets(items):
        weight = sum(item[1] for item in ss)
        value = sum(item[0] for item in ss)
        if weight > max_weight:
            continue
        if value > max_value:
            max_value = value
            max_value_set = ss
    return max_value_set
