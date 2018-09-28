import unittest

from algorithms.decrease_and_conquer import binary_search, insertion_sort
from .helper import StableSortTestBase


class BinarySearchTest(unittest.TestCase):
    def test_search_in_small_list(self):
        lst = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(binary_search(lst, 'a'), 0)
        self.assertEqual(binary_search(lst, 'b'), 1)
        self.assertEqual(binary_search(lst, 'c'), 2)
        self.assertEqual(binary_search(lst, 'd'), 3)
        self.assertEqual(binary_search(lst, 'e'), 4)

    def test_search_in_large_list(self):
        lst = list(range(1000))
        self.assertEqual(binary_search(lst, 765), 765)


class InsertionSortTest(unittest.TestCase, StableSortTestBase):
    def setUp(self):
        self.algorithm = insertion_sort
