import unittest

class TestSum(unittest.TestCase):


    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    # terminal returned nothing for this

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    # terminal returned "AssertionError: 5 != 6 : Should be 6"

if __name__ == "__main__":
    unittest.main()

# returned an AssertionError that said that the second test 
# failed, said "AssertionError: 5 != 6 : Should be 6", meaning 
# that there's a problem with the list amounts being summed or the method used
