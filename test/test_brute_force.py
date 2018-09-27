import unittest

from algorithms.brute_force import (
    bubble_sort, find_substring, linear_search, selection_sort
)
from .helper import FindSubstringTestBase, StableSortTestBase


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


if __name__ == '__main__':
    unittest.main()
