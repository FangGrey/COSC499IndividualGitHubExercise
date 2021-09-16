import unittest
from sortableArray import integerSort

class testSort(unittest.TestCase):
    def test(self):
        integerArray = [28, 18, 8, 15, 90, 3, 36, 47, 71]
        sortedIntegers = integerSort(integerArray)
        self.assertEqual((sortedIntegers), ([3, 8, 15, 18, 28, 36, 47, 71, 90]))

if __name__ == '__main__':
    unittest.main()