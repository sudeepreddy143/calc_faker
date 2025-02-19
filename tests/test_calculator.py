'''My Calculator Test'''
import pytest
from calculator import add, subtract
import random
from faker import Faker

fake = Faker()

@pytest.mark.parametrize("test_data", [
    {"a": fake.random_int(min=-100, max=100),
     "b": fake.random_int(min=-100, max=100),
     "operation": random.choice(["add", "subtract"])}
    for _ in range(10)
])
def test_operations(test_data):
    a, b, operation = test_data["a"], test_data["b"], test_data["operation"]

    if operation == "add":
        assert add(a, b) == a + b
    elif operation == "subtract":
        assert subtract(a, b) == a - b


def test_addition():
    '''Test that addition function works '''    
    assert add(1,7) == 8

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(7,4) == 3