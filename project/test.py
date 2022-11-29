import unittest

from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()




# command line "python -m unittest -v test" entry ran as expected before adding fraction test, ran 1 test with 'OK' return
# command line "python -m unittest discover" entry ran as expected before adding fraction test, ran 1 test with 'OK' return
# command line "python -m unittest discover" entry ran with fraction test, ran 2 tests, one failed, one passed
# using VSCode's debug tool set up with unittest also came to the same conclusion, saying that 9/10 does not equal 1