import unittest

from algorithms.decrease_and_conquer import insertion_sort
from .helper import StableSortTestBase


class InsertionSortTest(unittest.TestCase, StableSortTestBase):
    def setUp(self):
        self.algorithm = insertion_sort
