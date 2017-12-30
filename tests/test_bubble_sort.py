import unittest
from context import bubblesort

class BubbleSortTestCase(unittest.TestCase):
    def test_bubbleSort_succeeds(self):
        unsorted = [3, 6, 2, 1]
        sorted_list = [1, 2, 3, 6]
        result = bubblesort.bubbleSort(unsorted)
        self.assertEqual(result, sorted_list)

if __name__ == '__main__':
    unittest.main()