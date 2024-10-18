print("Calculator")

def getCalculation(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        return "None"

continue_calculation = True
isFirst = True
choice = 'n'
output = 0

while continue_calculation:
    if isFirst and choice != 'y' and choice == 'n':
        number1 = float(input("Enter first number: "))
    else:
        number1 = output
    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    number2 = float(input("Enter second number: "))
    output = getCalculation(number1, number2, operation)
    print(f"{number1} {operation} {number2} = {output}")

    choice = input(f"Type 'y' for continue calculating with {output}, or \nType 'n' to start a new calculation, or \nType 's' for stop calculation.").lower()
    if choice == 's':
        continue_calculation = False
