import unittest
from sortableArray import stringSort

class testSort(unittest.TestCase):
    def test(self):
        stringArray = ["White", "Black", "Red", "Blue", "Yellow", "Orange", "Grey", "Green", "Pink"]
        print(stringArray)
        sortedStrings = stringSort(stringArray)
        print(sortedStrings)
        self.assertEqual((sortedStrings), (["Black", "Blue", "Green", "Grey", "Orange", "Pink", "Red", "White", "Yellow"]))

if __name__ == '__main__':
    unittest.main()