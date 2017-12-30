import unittest
from context import bubble_sort

class BubbleSortTestCase(unittest.TestCase):
    def test_bubbleSort_succeeds(self):
        unsorted = [3, 6, 2, 1]
        sorted_list = [1, 2, 3, 6]
        result = bubble_sort.bubbleSort(unsorted)
        self.assertEqual(result, sorted_list)

if __name__ == '__main__':
    unittest.main()