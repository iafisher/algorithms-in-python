"""Brute-force and exhaustive search algorithms solve a problem by generating
all possible solutions until the correct one is found. Brute-force algorithms
are often simple to design and implement, but computationally expensive.

Backtracking, branch-and-bound and approximation can be used to improve the
performance of brute-force algorithms for problems with no known better
algorithms.

Author:  Ian Fisher (iafisher@protonmail.com)
Version: September 2018
"""

from .utils import enumerate_slice


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


def depth_first_search(graph):
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
    visited = {v: False for v in graph}
    for source in graph:
        if not visited[source]:
            yield from depth_first_search_helper(graph, source, visited)


def depth_first_search_helper(graph, source, visited):
    """Yield every vertex in the graph in depth-first order connected to the
    given vertex. `visited` should be a dictionary from vertices to booleans
    that indicate whether a vertex has been visited before.
    """
    yield source
    visited[source] = True
    for neighbor in graph[source]:
        if not visited[neighbor]:
            yield from depth_first_search_helper(graph, neighbor, visited)


def breadth_first_search(graph):
    """Yield every vertex in the graph (represented as an adjacency list) in
    breadth-first order, i.e. starting at an arbitrary root and visiting each of
    its neighbors before visiting the neighbors of the root's first neighbors,
    and so on.

    Design idea: Similar to depth-first search, we will use a helper function
    to visit all the vertices of a connected subgraph.

    Complexity: O(|V| + |E|) time, O(|V|) space.
    """
    visited = {v: False for v in graph}
    for source in graph:
        if not visited[source]:
            yield from breadth_first_search_helper(graph, source, visited)


def breadth_first_search_helper(graph, source, visited):
    """Yield every vertex in the graph in breadth-first order connected to the
    given vertex. `visited` should be a dictionary from vertices to booleans
    that indicate whether a vertex has been visited before.
    """
    yield source
    visited[source] = True
    queue = [source]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                yield neighbor
                visited[neighbor] = True
                queue.append(neighbor)


def closest_pair(points: list) -> tuple:
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
        for j, p2 in enumerate_slice(points, i+1):
            # Note that for comparison purposes we do not need to compute the
            # square root to get the actual distance.
            distance = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
            if closest_distance is None or distance < closest_distance:
                closest_distance = distance
                closest_pair = (p1, p2)
    return closest_pair
