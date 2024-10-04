def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def main():
    # Get two numbers from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    print(f"{number1} + {number2} = {addition(number1, number2)}")
    print(f"{number1} - {number2} = {subtraction(number1, number2)}")
if __name__ == '__main__':
    main()
