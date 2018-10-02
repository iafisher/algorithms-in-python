import unittest

from algorithms.decrease_and_conquer import (
    binary_search, insertion_sort, subsets
)
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


class SubsetsTest(unittest.TestCase):
    def test_empty_set(self):
        self.assertSetEqual(set(subsets(set())), self.to_frozenset([set()]))

    def test_singleton_set(self):
        self.assertSetEqual(
            set(subsets({'a'})),
            self.to_frozenset([set(), {'a'}])
        )

    def test_set_with_two_elements(self):
        self.assertSetEqual(
            set(subsets({'a', 'b'})),
            self.to_frozenset([set(), {'a'}, {'b'}, {'a', 'b'}])
        )

    def test_set_with_three_elements(self):
        s = {'a', 'b', 'c'}
        self.assertSetEqual(
            set(subsets(s)),
            self.to_frozenset([
                set(), {'a'}, {'b'}, {'a', 'b'}, {'c'}, {'b', 'c'}, {'a', 'c'},
                {'a', 'b', 'c'}
            ])
        )

    def test_set_with_five_elements(self):
        s = {'a', 'b', 'c', 'd', 'e'}
        self.assertSetEqual(
            set(subsets(s)),
            self.to_frozenset([
                set(), {'a'}, {'b'}, {'c'}, {'d'}, {'e'}, {'a', 'b'},
                {'a', 'c'}, {'a', 'd'}, {'a', 'e'}, {'b', 'c'}, {'b', 'd'},
                {'b', 'e'}, {'c', 'd'}, {'c', 'e'}, {'d', 'e'}, {'a', 'b', 'c'},
                {'a', 'b', 'd'}, {'a', 'b', 'e'}, {'a', 'c', 'd'},
                {'a', 'c', 'e'}, {'a', 'd', 'e'}, {'b', 'c', 'd'},
                {'b', 'c', 'e'}, {'b', 'd', 'e'}, {'c', 'd', 'e'},
                {'a', 'b', 'c', 'd'}, {'a', 'b', 'c', 'e'},
                {'a', 'b', 'd', 'e'}, {'a', 'c', 'd', 'e'},
                {'b', 'c', 'd', 'e'}, {'a', 'b', 'c', 'd', 'e'}
            ])
        )

    def test_set_with_twelve_elements(self):
        s = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'}
        self.assertEqual(len(list(subsets(s))), 2**12)

    def to_frozenset(self, s):
        """Helper function to convert a list of sets into a frozenset of
        frozensets.
        """
        return frozenset(frozenset(x) for x in s)
