This is my repository

# Directory Structure 
    1. Calculator
        a. __init__.py -> Contains Arithmetic Methods for performing calculations
        b. calculation.py -> Contains Classes for handling Calculation history and Operations

    2. tests
        a. __init__.py
        b. test_calculator.py -> contains coverage tests for all methods and error handling

# How to Run Tests
Navigate to the working directory of the calculator project via Terminal and use the below commands
1. pytest -v tests (Runs the test cases located in the tests directory)

2. pytest --cov=calculator --cov-report=term-missing (Runs the tests while measuring code coverage for the calculator module and isplays a coverage report in the terminal, highlighting which lines of code were missed)

3. pytest --pylint --cov (Runs to to check for coding standard violations and also runs tests  while measuring test coverage )

