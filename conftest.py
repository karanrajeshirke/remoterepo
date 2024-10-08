import pytest

# Sample fixture that sets up some initial data
@pytest.fixture
def sample_data():
    return "no sample data currently avaiable"

# Another fixture that creates a list of numbers
@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]

# Test function that uses the sample_data fixture
def test_name(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["name"] == "Karan"

# Test function that uses the number_list fixture
def test_number_list_sum(number_list):
    assert sum(number_list) == 15

# Test function that checks if a number is in the list
def test_number_in_list(number_list):
    assert 3 in number_list

# A more complex test that uses both fixtures
def test_combined_fixtures(sample_data, number_list):
    assert sample_data["city"] == "Wonderland"
    assert len(number_list) == 5
    assert sum(number_list) + sample_data["age"] == 45



def newfunc():
    print("this is a new function which is to be added to all branched")
    
def ipconfig():
    return "ipconfig"

