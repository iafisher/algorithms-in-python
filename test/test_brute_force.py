import unittest

from algorithms.brute_force import (
    breadth_first_search, bubble_sort, depth_first_search, find_substring,
    linear_search, selection_sort
)
from .helper import (
    FindSubstringTestBase, StableSortTestBase, GRAPH_3_10, GRAPH_3_12A,
    GRAPH_3_12B
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


class SelectionSortTest(unittest.TestCase, StableSortTestBase):
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
