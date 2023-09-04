def perform_calculation(number1, number2):
    try:
        result = number1 * number2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter an integer.")
# Test case
number1=float(input("Enter the first number:-"))
number2=float(input("Enter the second number:-"))
perform_calculation(number1,number2)
