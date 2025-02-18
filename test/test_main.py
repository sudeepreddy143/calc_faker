import pytest
from main import calculate_and_print  # Ensure this import path matches your project structure

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_output", [
    ("7", "2", "add", "The result of 7 add 2 is 9"),
    ("15", "5", "subtract", "The result of 15 subtract 5 is 10"),
    ("6", "3", "multiply", "The result of 6 multiply 3 is 18"),
    ("25", "5", "divide", "The result of 25 divide 5 is 5"),
    ("8", "0", "divide", "Error: Division by zero."),  # Testing division by zero error message
    ("12", "4", "unknown", "Unknown operation: unknown"),  # Testing an invalid operation
    ("x", "3", "add", "Invalid number input: x or 3 is not a valid number."),  # Invalid number input test
    ("9", "y", "subtract", "Invalid number input: 9 or y is not a valid number.")  # Another invalid number input
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_output, capsys):
    """Test the calculate_and_print function with different inputs and expected outputs."""
    calculate_and_print(a_string, b_string, operation_string)
    
    # Capture printed output
    captured = capsys.readouterr()
    
    # Assert that output matches expected output
    assert captured.out.strip() == expected_output
