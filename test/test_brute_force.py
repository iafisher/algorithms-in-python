import unittest

from algorithms.brute_force import (
    breadth_first_search, bubble_sort, closest_pair, convex_hull,
    depth_first_search, find_substring, knapsack, linear_search, permutations,
    selection_sort, traveling_salesman,
)
from .helper import (
    ClosestPairTestBase, ConvexHullTestBase, FindSubstringTestBase,
    KnapsackTestBase, StableSortTestBase, SortTestBase,
    TravelingSalesmanTestBase, GRAPH_3_10, GRAPH_3_12A, GRAPH_3_12B,
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
        vertices = list(depth_first_search(GRAPH_3_10))
        self.assertEqual(
            vertices, ['a', 'c', 'd', 'f', 'b', 'e', 'g', 'h', 'i', 'j']
        )

    def test_graph_3_12a(self):
        vertices = list(depth_first_search(GRAPH_3_12A))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'h', 'g', 'f', 'e'])

    def test_graph_3_12b(self):
        vertices = list(depth_first_search(GRAPH_3_12B))
        self.assertEqual(vertices, ['a', 'b', 'c', 'd', 'g', 'f', 'e'])


class BreadthFirstSearchTest(unittest.TestCase):
    def test_graph_3_10(self):
        vertices = list(breadth_first_search(GRAPH_3_10))
        self.assertEqual(
            vertices, ['a', 'c', 'd', 'e', 'f', 'b', 'g', 'h', 'j', 'i']
        )

    def test_graph_3_12a(self):
        vertices = list(breadth_first_search(GRAPH_3_12A))
        self.assertEqual(vertices, ['a', 'b', 'e', 'c', 'f', 'd', 'g', 'h'])

    def test_graph_3_12b(self):
        vertices = list(breadth_first_search(GRAPH_3_12B))
        self.assertEqual(vertices, ['a', 'b', 'e', 'c', 'f', 'd', 'g'])


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
