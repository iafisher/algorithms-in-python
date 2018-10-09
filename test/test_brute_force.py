import unittest

from algorithms.brute_force import (
    breadth_first_search, bubble_sort, closest_pair, convex_hull,
    depth_first_search, detect_cycle, find_substring, knapsack, linear_search,
    permutations, selection_sort, traveling_salesman,
)
from .base import (
    ClosestPairTestBase, ConvexHullTestBase, FindSubstringTestBase,
    KnapsackTestBase, StableSortTestBase, SortTestBase,
    TravelingSalesmanTestBase, 
)
from .examples import (
    GRAPH_3_7, GRAPH_3_10, GRAPH_3_12A, GRAPH_3_12B, GRAPH_4_5, 
    GRAPH_4_2_EX_1A, GRAPH_4_2_EX_1B, GRAPH_4_6,
)


class LinearSearchTest(unittest.TestCase):
    def test_basic(self):
        lst = ['Latvia', 'Lithuania', 'Estonia']
        self.assertEqual(linear_search(lst, 'Estonia'), 2)
        self.assertEqual(linear_search(lst, 'Lithuania'), 1)
        self.assertEqual(linear_search(lst, 'Latvia'), 0)

    def test_nonexistent_element(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(lst, 6), -1)
        self.assertEqual(linear_search(lst, 'not me'), -1)


class SelectionSortTest(unittest.TestCase, SortTestBase):
    def setUp(self):
        self.algorithm = selection_sort


class BubbleSortTest(unittest.TestCase, StableSortTestBase):
    def setUp(self):
        self.algorithm = bubble_sort


class FindSubstringTest(unittest.TestCase, FindSubstringTestBase):
    def setUp(self):
        self.algorithm = find_substring


class DepthFirstSearchTest(unittest.TestCase):
    def test_graph_3_10(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_3_10))
        self.assertEqual(
            vertices, ['a', 'c', 'd', 'f', 'b', 'e', 'g', 'h', 'i', 'j']
        )

    def test_graph_3_12a(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_3_12A))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'h', 'g', 'f', 'e'])

    def test_graph_3_12b(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_3_12B))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'g', 'f', 'e'])

    def test_graph_4_5(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_4_5))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'e'])

    def test_graph_4_6(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_4_6))
        self.assertEqual(vertices, ['C1', 'C3', 'C4', 'C5', 'C2'])

    def test_graph_4_2_ex_1a(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_4_2_EX_1A))
        self.assertEqual(vertices, ['a', 'b', 'e', 'g', 'f', 'c', 'd'])

    def test_graph_4_2_ex_1b(self):
        # Note that this is not the only valid DFS traversal of this graph.
        vertices = list(depth_first_search(GRAPH_4_2_EX_1B))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'g', 'e', 'f'])


class BreadthFirstSearchTest(unittest.TestCase):
    def test_graph_3_10(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_3_10))
        self.assertEqual(
            vertices, ['a', 'c', 'd', 'e', 'f', 'b', 'g', 'h', 'j', 'i']
        )

    def test_graph_3_12a(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_3_12A))
        self.assertEqual(vertices, ['a', 'b', 'e', 'c', 'f', 'd', 'g', 'h'])

    def test_graph_3_12b(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_3_12B))
        self.assertEqual(vertices, ['a', 'b', 'e', 'c', 'f', 'd', 'g'])

    def test_graph_4_5(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_4_5))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'e'])

    def test_graph_4_6(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_4_6))
        self.assertEqual(vertices, ['C1', 'C3', 'C4', 'C5', 'C2'])

    def test_graph_4_2_ex_1a(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_4_2_EX_1A))
        self.assertEqual(vertices, ['a', 'b', 'c', 'e', 'g', 'f', 'd'])

    def test_graph_4_2_ex_1b(self):
        # Note that this is not the only valid BFS traversal of this graph.
        vertices = list(breadth_first_search(GRAPH_4_2_EX_1B))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'g', 'e', 'f'])


class ClosestPairTest(unittest.TestCase, ClosestPairTestBase):
    def setUp(self):
        self.algorithm = closest_pair


class ConvexHullTest(unittest.TestCase, ConvexHullTestBase):
    def setUp(self):
        self.algorithm = convex_hull


class TravelingSalesmanTest(unittest.TestCase, TravelingSalesmanTestBase):
    def setUp(self):
        self.algorithm = traveling_salesman


class PermutationsTest(unittest.TestCase):
    def test_two_items(self):
        items = ['a', 'b']
        self.assertEqual(list(permutations(items)), [('a', 'b'), ('b', 'a')])

    def test_three_items(self):
        items = ['a', 'b', 'c']
        self.assertEqual(
            list(permutations(items)),
            [
                ('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'),
                ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')
            ]
        )

    def test_four_items(self):
        items = ['a', 'b', 'c', 'd']
        self.assertEqual(
            list(permutations(items)),
            [
               ('a', 'b', 'c', 'd'), ('a', 'b', 'd', 'c'), ('a', 'c', 'b', 'd'),
               ('a', 'c', 'd', 'b'), ('a', 'd', 'b', 'c'), ('a', 'd', 'c', 'b'),
               ('b', 'a', 'c', 'd'), ('b', 'a', 'd', 'c'), ('b', 'c', 'a', 'd'),
               ('b', 'c', 'd', 'a'), ('b', 'd', 'a', 'c'), ('b', 'd', 'c', 'a'),
               ('c', 'a', 'b', 'd'), ('c', 'a', 'd', 'b'), ('c', 'b', 'a', 'd'),
               ('c', 'b', 'd', 'a'), ('c', 'd', 'a', 'b'), ('c', 'd', 'b', 'a'),
               ('d', 'a', 'b', 'c'), ('d', 'a', 'c', 'b'), ('d', 'b', 'a', 'c'),
               ('d', 'b', 'c', 'a'), ('d', 'c', 'a', 'b'), ('d', 'c', 'b', 'a')
            ]
        )

    def test_zero_items(self):
        self.assertEqual(list(permutations([])), [])

    def test_one_item(self):
        self.assertEqual(list(permutations(['a'])), [('a',)])


class KnapsackTest(unittest.TestCase, KnapsackTestBase):
    def setUp(self):
        self.algorithm = knapsack


class DetectCycleTest(unittest.TestCase):
    def test_graph_3_7(self):
        self.assertTrue(detect_cycle(GRAPH_3_7))

    def test_graph_3_10(self):
        self.assertTrue(detect_cycle(GRAPH_3_10))

    def test_graph_3_12a(self):
        self.assertTrue(detect_cycle(GRAPH_3_12A))

    def test_graph_3_12b(self):
        self.assertTrue(detect_cycle(GRAPH_3_12B))

    def test_graph_4_5(self):
        self.assertTrue(detect_cycle(GRAPH_4_5))

    def test_graph_4_6(self):
        self.assertFalse(detect_cycle(GRAPH_4_6))

    def test_graph_4_2_ex_1a(self):
        self.assertFalse(detect_cycle(GRAPH_4_2_EX_1A))

    def test_graph_4_2_ex_1b(self):
        self.assertTrue(detect_cycle(GRAPH_4_2_EX_1B))
