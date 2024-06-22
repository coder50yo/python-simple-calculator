# calculator.py

def add(x, y):
    """
    This function adds two numbers together.

    Parameters:
    x (int or float): The first number to add.
    y (int or float): The second number to add.

    Returns:
    int or float: The sum of x and y.
    """
    return x + y
def subtract(x, y):
    """
    This function subtracts two numbers.

    Parameters:
    x (int or float): The first number from which the second number is to be subtracted.
    y (int or float): The second number which is to be subtracted from the first number.

    Returns:
    int or float: The result of the subtraction.
    """
    return x - y
def multiply(x, y):
    """
    Function to multiply two numbers

    Parameters:
    x (int or float): The first number to multiply
    y (int or float): The second number to multiply

    Returns:
    int or float: The product of x and y
    """
    return x * y
def divide(x, y):
    """
    Function to divide two numbers.
    
    Args:
        x (float): The dividend.
        y (float): The divisor.
        
    Returns:
        float: The result of the division operation.
        
    Raises:
        ValueError: If the divisor is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
if __name__ == "__main__":
    print("Welcome to the calculator app!")
    print("Operations available:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter operation (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = None

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print("Error:", e)
            exit(1)
    else:
        print("Invalid choice")

    print("Result:", result)