import sys
from calculator import add, subtract

def main():
    try:
        a, b, operation = sys.argv[1], sys.argv[2], sys.argv[3]
        
        # Ensure inputs are valid numbers
        try:
            a, b = int(a), int(b)
        except ValueError:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
            return
        
        # Perform the operation
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        # elif operation == "multiply":
        #     result = multiply(a, b)
        # elif operation == "divide":
        #     result = divide(a, b)
        else:
            print(f"Unknown operation: {operation}")
            return
        
        print(f"The result of {a} {operation} {b} is equal to {result}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

