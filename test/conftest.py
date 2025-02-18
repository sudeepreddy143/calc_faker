import pytest
from decimal import Decimal
from faker import Faker
from calculator import Calculator

fake = Faker()

def generate_test_data(num_records):
    """Generates test data dynamically for Calculator operations."""
    
    # Mapping operations to Calculator methods
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    for _ in range(num_records):
        # Generate two random decimal numbers
        a = Decimal(fake.random_int(min=1, max=99))
        b = Decimal(fake.random_int(min=1, max=99))

        # Randomly select an operation
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        # Handle division edge case
        if operation_func == Calculator.divide:
            b = Decimal(fake.random_int(min=1, max=99))  # Ensure b is not zero

        # Compute expected result
        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, expected

def pytest_addoption(parser):
    """Allows setting number of test records from CLI."""
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

@pytest.fixture(params=[(a, b, operation, expected) for a, b, operation, expected in generate_test_data(5)])
def test_data(request):
    """Fixture that provides dynamically generated test data."""
    return request.param

