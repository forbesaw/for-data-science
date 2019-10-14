# -*- coding: utf-8 -*-

# Estimate interest
print("")
print("")

print("Welcome to the compound interest calculator!")
print("")
print("Select [1] as United States")  # USD
print("Select [2] as European Union")  # EUR
print("Select [3] as United Kingdom")  # GBP
print("Select [4] as World Citizen")  # BTC
print("")

while True:
    try:
        choice = int(raw_input("Please Select Country: "))
        if choice not in [1, 2, 3, 4]:
            print("Number not in range. Please try again...")
            continue
    except ValueError:
        print("Oops!  That was no valid number. Try again...")
    else:
        break


def userChoiceCur():

    if choice == 1:
        cur_sym = "$"
        return cur_sym

    if choice == 2:
        cur_sym = "€"
        return cur_sym

    if choice == 3:
        cur_sym = "£"
        return cur_sym

    if choice == 4:
        cur_sym = "₿"
        return cur_sym


def userChoiceRate():

    if choice == 1:
        inflation_rate = 1.02  # will call API stored values?
        return inflation_rate

    if choice == 2:
        inflation_rate = 1.0000
        return inflation_rate

    if choice == 3:
        inflation_rate = 1.0075
        return inflation_rate

    if choice == 4:
        inflation_rate = 1.0000
        return inflation_rate


print("")

print("Enter period of interest (years)")
years = int(raw_input("Enter years: "))

print("What is the initial principal?")
principal = float(raw_input("Enter principal: "))

print("What are the monthly contributions?")
contributions = float(raw_input("Enter amount: "))

print("What is the APR (in decimal format)?")
APR = float(raw_input("Enter percentage: "))

print(" ")

contributions = contributions * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + contributions) * (1 + APR)
    final_output = (
        "Final amount gained after {} years: ".format(years)
        + userChoiceCur()
        + "{:,}".format(round(final_amount, 2))
        + " at a {:.2%} APR ".format(APR)
    )

print("")
print(final_output)
print("")
print("")
