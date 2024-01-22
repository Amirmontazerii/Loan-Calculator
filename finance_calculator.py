''' This is a python program that calculate the intrest of
simple and compound invesment and the amount of that you'll
have to pay on a home loan '''

import math

# displaying two calculator that user can choose theme
print("1. Investment Calculator")
print("2. Bond Calculator")

# taking user's entrie for calculators
choice = input("Choose a calculator (1 or 2): ")
# making conditons for users's choice
if choice == "1":
    # Input for investment calculator
    principal = float(
        input("Enter the amount of money you want to deposite: "))
    interest_rate = float(
        input("Enter the interest rate : ")) / 100
    years = int(input("Enter the number of years you plan to investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculating total amount based on interest type
    if interest_type == "simple":
        total_amount = principal * (1 + interest_rate * years)
    elif interest_type == "compound":
        total_amount = principal * (1 + interest_rate) ** years
    else:
        # Handling invalid interest type
        print("Invalid interest type. Please choose 'simple' or 'compound'.")
        exit()

    # Displaying the result for investment calculator
    print(f"The total amount after {years} years will be: {total_amount:.2f}")

elif choice == "2":
    # Input for bond calculator
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(
        input("Enter the annual interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months for repayment: "))

    # Calculating monthly repayment amount for the bond
    monthly_repayment = (interest_rate / 12 * present_value) / \
        (1 - (1 + interest_rate / 12) ** -months)

    # Displaying the result for the bond calculator
    print(
        f"The monthly repayment amount for the bond will be: {monthly_repayment:.2f}")

else:
    # Handling invalid choice
    print("Invalid choice. Please enter 1 or 2.")
