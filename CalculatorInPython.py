def Calculator(firstNumber, secondNumber, operator):
    if operator == "+":
        return firstNumber + secondNumber
    elif operator == "-":
        return firstNumber - secondNumber
    elif operator == "*":
        return firstNumber * secondNumber
    elif operator == "/":
        if secondNumber == 0:
            return "Error: Division by zero is not allowed"
        return firstNumber // secondNumber
    else:
        raise ValueError('Invalid Operator')

if __name__ == "__main__":
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))
    operator = input("Enter an operator (+,-,*,/): ")
    result=Calculator(firstNumber, secondNumber, operator)
    print(result)
