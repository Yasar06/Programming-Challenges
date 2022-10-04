def choice():
    choice = 0
    while choice != "q":
        choice = input("press 'q' to quit or any other key to enter a calulation\n")
        if choice == "q":
            quit()
        else:
            calculator()

def calculator():
            
        operand1 = int(input("enter operand 1\n"))            
        operand2 = int(input("enter operand 2\n"))
        operator = input("enter operator\n")
        if operator == "+":
            calculation = operand1 + operand2
        elif operator == "-":
            calculation = operand1 - operand2
        elif operator =="*":
            calculation = operand1 * operand2
        elif operator == "/":
            calculation = operand1 / operand2
        elif operator == "//":
            calculation = operand1 // operand2
        elif operator == "%":
            calculation = operand1 % operand2
        elif operator == "**":
            calculation = operand1 ** operand2

        print(calculation)

if __name__ == '__main__':
    choice()
