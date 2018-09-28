"""Collected test cases for problems with multiple algorithms solving them.

Use these classes by inheriting from them and unittest.TestCase, and defining a
setUp method that sets `self.algorithm` to the desired algorithm, e.g.

class BogoSortTest(unittest.TestCase, SortTestBase):
    def setUp(self):
        self.algorithm = bogosort

"""
import functools
import unittest


class SortTestBase:
    """A base class for testing sorting algorithms. The sorting algorithm should
    take a list of orderable values as its only argument, and return the list
    sorted in ascending order. The sort should not be stable. For stable sorts,
    use StableSortTestBase instead.
    """

    def test_basic(self):
        lst = [9, -1, 4, 2]
        self.assertEqual(self.algorithm(lst), [-1, 2, 4, 9])

    def test_already_sorted(self):
        lst = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.algorithm(lst), [1, 2, 3, 4, 5, 6, 7])

    def test_already_sorted_in_descending_order(self):
        lst = [7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(self.algorithm(lst), [1, 2, 3, 4, 5, 6, 7])

    def test_big_example(self):
        lst = [
            -33, 37, -83, 9, -59, 72, -91, -82, 52, 69, -34, -7, 43, -92, -96,
            -66, 81, 48, 91, 45, -2, 26, -20, -42, 16, -36, -19, -77, -17, -15,
            -40, 69, -59, -6, 13, 54, 86, -79, 14, 49, 88, -34, 88, 40
        ]
        self.assertEqual(
            self.algorithm(lst),
            [
                -96, -92, -91, -83, -82, -79, -77, -66, -59, -59, -42, -40, -36,
                -34, -34, -33, -20, -19, -17, -15, -7, -6, -2, 9, 13, 14, 16,
                26, 37, 40, 43, 45, 48, 49, 52, 54, 69, 69, 72, 81, 86, 88, 88,
                91
            ]
        )

    def test_another_big_example(self):
        lst = [
            66, -93, 17, 2, 64, 45, -100, -22, -24, -100, -88, -88, -36, -92,
            14, 4, -2, -61, -7, -64, -100, -66, -52, 96, 24, -72, 26, 21, -48,
            -26, -10, -16, 10, -3, 79, -24, 73, -23, -34, -64, -19, 70, 99
        ]
        self.assertEqual(
            self.algorithm(lst),
            [
                -100, -100, -100, -93, -92, -88, -88, -72, -66, -64, -64, -61,
                -52, -48, -36, -34, -26, -24, -24, -23, -22, -19, -16, -10, -7,
                -3, -2, 2, 4, 10, 14, 17, 21, 24, 26, 45, 64, 66, 70, 73, 79,
                96, 99
            ]
        )

    def test_list_of_strings(self):
        lst = ['Shikoku', 'Honshu', 'Kyushu', 'Hokkaido']
        self.assertEqual(
            self.algorithm(lst), ['Hokkaido', 'Honshu', 'Kyushu', 'Shikoku']
        )


class StableSortTestBase(SortTestBase):
    """Same as SortTestBase, but with additional tests for stable sorts."""

    def test_sort_stability(self):
        b = DummyObject('b')
        a0 = DummyObject('a')
        a1 = DummyObject('a')
        lst = [b, a0, a1]
        sorted_lst = self.algorithm(lst)
        self.assertEqual(sorted_lst, [a0, a1, b])
        # Make sure a0 and a1 are in their original order.
        self.assertIs(sorted_lst[0], a0)
        self.assertIs(sorted_lst[1], a1)

    def test_sort_stability_again(self):
        a = DummyObject('a')
        b0 = DummyObject('b')
        b1 = DummyObject('b')
        lst = [b0, a, b1]
        sorted_lst = self.algorithm(lst)
        self.assertEqual(sorted_lst, [a, b0, b1])
        # Make sure b0 and b1 are in their original order.
        self.assertIs(sorted_lst[1], b0)
        self.assertIs(sorted_lst[2], b1)


@functools.total_ordering
class DummyObject:
    """A dummy object for testing sort stability. Defined so that `x == y` does
    not imply `x is y`.
    """

    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return f'<DummyObject({repr(self.data)}) at {hex(id(self))}>'


class FindSubstringTestBase:
    """A base class for testing string matching algorithms. The algorithm should
    take two arguments, a text and a pattern, and return the index of the first
    letter of the first occurrence of the pattern in the text, or -1 if the
    pattern does not occur.
    """

    def test_one_letter_pattern(self):
        self.assertEqual(self.algorithm('abc', 'c'), 2)

    def test_multi_letter_pattern(self):
        self.assertEqual(self.algorithm('racecar', 'ace'), 1)

    def test_empty_text(self):
        self.assertEqual(self.algorithm('', 'datum'), -1)

    def test_empty_pattern(self):
        self.assertEqual(self.algorithm('Lorem ipsum', ''), 0)

    def test_pattern_equals_text(self):
        self.assertEqual(self.algorithm('twin', 'twin'), 0)

    def test_pattern_longer_than_text(self):
        self.assertEqual(self.algorithm('Guinea', 'Guinea-Bissau'), -1)

    def test_almost_match(self):
        self.assertEqual(self.algorithm('water bottle', 'waiter'), -1)

    def test_another_almost_match(self):
        self.assertEqual(self.algorithm('cockpit', 'pita'), -1)


# Figure 3.10 on page 123
GRAPH_3_10 = {
    'a': ['c', 'd', 'e'],
    'b': ['e', 'f'],
    'c': ['a', 'd', 'f'],
    'd': ['a', 'c'],
    'e': ['a', 'b', 'f'],
    'f': ['b', 'c', 'e'],
    'g': ['h', 'j'],
    'h': ['i', 'g'],
    'i': ['h', 'j'],
    'j': ['i', 'g'],
}


# Figure 3.12a on page 127
GRAPH_3_12A = {
    'a': ['b', 'e'],
    'b': ['a', 'c', 'f'],
    'c': ['b', 'd', 'g'],
    'd': ['c', 'h'],
    'e': ['a', 'f'],
    'f': ['b', 'e', 'g'],
    'g': ['c', 'f', 'h'],
    'h': ['d', 'g'],
}


# Figure 3.12b on page 127
GRAPH_3_12B = {
    'a': ['b', 'e'],
    'b': ['a', 'c', 'f'],
    'c': ['b', 'd', 'g'],
    'd': ['c'],
    'e': ['a'],
    'f': ['b'],
    'g': ['c'],
}
