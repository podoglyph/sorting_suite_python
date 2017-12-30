import unittest
from context import insertion_sort

class InsertionSortTestCase(unittest.TestCase):
    def test_insertionSort_succeeds(self):
        unsorted = [3, 6, 2, 1]
        sorted_list = [1, 2, 3, 6]
        result = insertion_sort.insertionSort(unsorted)
        self.assertEqual(result, sorted_list)

if __name__ == '__main__':
    unittest.main()