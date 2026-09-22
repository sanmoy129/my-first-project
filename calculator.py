# Simple Python Calculator

def calculator():
    print("===== Python Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    while True:
        choice = input("\nEnter your choice (1-6): ")

        if choice == "6":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Please select 1-6.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                print("Result:", result)

            elif choice == "2":
                result = num1 - num2
                print("Result:", result)

            elif choice == "3":
                result = num1 * num2
                print("Result:", result)

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print("Result:", result)

            elif choice == "5":
                if num2 == 0:
                    print("Error: Cannot use zero for modulus!")
                else:
                    result = num1 % num2
                    print("Result:", result)

        except ValueError:
            print("Please enter valid numbers!")


# Run the calculator
calculator()
