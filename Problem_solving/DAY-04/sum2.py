num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
choice = str(input("Enter the choice: "))
match choice:
    case "+":
        print(f'{num1}+{num2}={num1+num2}')
    case "-":
        print(f'{num1}-{num2}={num1-num2}')
    case "*":
        print(f'{num1}*{num2}={num1*num2}')
    case "/":
        print(f'{num1}/{num2}={num1/num2}')