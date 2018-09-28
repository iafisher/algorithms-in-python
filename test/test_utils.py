import unittest

from algorithms.utils import iterate_slice


class IterateSliceTest(unittest.TestCase):
    def test_slice_off_beginning(self):
        slce = list(iterate_slice(['a', 'b', 'c', 'd'], 1))
        self.assertEqual(slce, ['b', 'c', 'd'])

    def test_slice_off_end(self):
        slce = list(iterate_slice(['a', 'b', 'c', 'd'], 0, 3))
        self.assertEqual(slce, ['a', 'b', 'c'])

    def test_slice_off_beginning_and_end(self):
        slce = list(iterate_slice(['a', 'b', 'c', 'd'], 1, 3))
        self.assertEqual(slce, ['b', 'c'])

    def test_slice_whole_list(self):
        slce = list(iterate_slice(['a', 'b', 'c', 'd'], 0))
        self.assertEqual(slce, ['a', 'b', 'c', 'd'])
