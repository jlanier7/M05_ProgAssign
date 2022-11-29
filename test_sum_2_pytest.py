def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

# terminal returned nothing for this

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

# terminal returned "AssertionError: Should be 6"

"""
Used pytest in the command line via 
> pytest test_sum_2_pytest.py
and it automatically ran the test on the file and gave me line by line execution of the assertions. Knowing that sum() is a pretty reliable
function I can assume the sum tuple elements are the issue. It's also nice that it gives a short test summary at the end."""