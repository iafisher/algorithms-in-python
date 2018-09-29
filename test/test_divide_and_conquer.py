import unittest

from algorithms.divide_and_conquer import merge, merge_sort
from .helper import StableSortTestBase


class MergeSortTest(unittest.TestCase, StableSortTestBase):
    def setUp(self):
        self.algorithm = merge_sort


class MergeTest(unittest.TestCase):
    def merge_lists_of_equal_lengths(self):
        lst1 = [-10, 0, 1, 1, 4]
        lst2 = [-5, -2, -1, 7, 8]
        into = [0] * 10
        merge(lst1, lst2, into)
        self.assertEqual(into, [-10, -5, -2, -1, 0, 1, 1, 4, 7, 8])

    def merge_lists_of_unequal_lengths(self):
        lst1 = [1, 4, 6, 9]
        lst2 = [2, 3, 5, 10, 13]
        into = [0] * 9
        merge(lst1, lst2, into)
        self.assertEqual(into, [1, 2, 3, 4, 5, 6, 9, 10, 13])

    def merge_non_overlapping_lists(self):
        lst1 = [-3, -2, -1, 0]
        lst2 = [1, 2, 3, 4]
        into = [0] * 8
        merge(lst1, lst2, into)
        self.assertEqual(into, [-3, -2, -1, 0, 1, 2, 3, 4])

    def merge_empty_lists(self):
        into = []
        merge([], [], into)
        self.assertEqual(into, [])

    def merge_empty_and_non_empty_list(self):
        into = [0] * 3
        merge([1, 2, 3], [], into)
        self.assertEqual(into, [1, 2, 3])
