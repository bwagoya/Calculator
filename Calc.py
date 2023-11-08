def main():
    # Letting the user decide what operation they want to use
    num1 = float(input("Enter a number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter a number: "))

    if op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        if num2 != 0:  # Check for division by zero
            print(num1 / num2)
        else:
            print("Error: Division by zero")
    else:
        print("Invalid Operator!!")

if __name__ == "__main__":
    main()