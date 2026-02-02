import pytest

@pytest.fixture
def setup():
    print("This is setup")
    
def test_setup(setup):
    print("This is post setup")