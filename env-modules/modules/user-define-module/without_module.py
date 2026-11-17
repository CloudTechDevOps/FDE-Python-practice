def addition (a, b):
    return a + b

def subtraction (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    return a / b if b != 0 else "Error: Division by zero is not allowed."

def main():
    print ("addition", addition(10, 5))
    print ("subtraction", subtraction(10, 5))
    print ("multiplication", multiplication(10, 5))
    print ("division", division(10, 5))

if __name__ == "__main__":
    main()