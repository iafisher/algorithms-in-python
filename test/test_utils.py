import unittest

from algorithms.utils import enumerate_slice


class EnumerateSliceTest(unittest.TestCase):
    def test_slice_off_beginning(self):
        slce = list(enumerate_slice(['a', 'b', 'c', 'd'], 1))
        self.assertEqual(slce, [(1, 'b'), (2, 'c'), (3, 'd')])

    def test_slice_off_end(self):
        slce = list(enumerate_slice(['a', 'b', 'c', 'd'], 0, 3))
        self.assertEqual(slce, [(0, 'a'), (1, 'b'), (2, 'c')])

    def test_slice_off_beginning_and_end(self):
        slce = list(enumerate_slice(['a', 'b', 'c', 'd'], 1, 3))
        self.assertEqual(slce, [(1, 'b'), (2, 'c')])

    def test_slice_whole_list(self):
        slce = list(enumerate_slice(['a', 'b', 'c', 'd'], 0))
        self.assertEqual(slce, [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')])
