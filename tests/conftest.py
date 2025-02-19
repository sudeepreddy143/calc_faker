import pytest
import random
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records")

@pytest.fixture(scope="module", params=range(10))  # Default 10 tests
def test_data(request):
    return {
        "a": fake.random_int(min=-100, max=100),
        "b": fake.random_int(min=-100, max=100),
        "operation": random.choice(["add", "subtract"])
    }
