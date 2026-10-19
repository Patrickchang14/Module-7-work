# M7P5 Module 7 Patrick Chang Oct 18, 2026

# Declare variable
total_discounts = 0

# Prompt user
continue_program = input("Do you want to run this program? (Yes/No): ")

# While loop
while continue_program.lower() == "yes":
    quantity = float(input("Enter quantity of item: "))
    price = float(input("Enter price of item: "))

# Calculation
    extended_price = quantity * price

    # If statements
    if extended_price > 10000.00:
        discount_rate = 0.25
    else:
        discount_rate = 0.10

    # Calculations
    discount_amount = extended_price * discount_rate
    total = extended_price - discount_amount

    # Increments
    total_discounts += discount_amount

    # Outputs
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Total: ${total:.2f}")

    # Prompt user for second loop
    continue_program = input("Do you want to run the program again? (Yes/No): ")

# Outputs for second loop
print(f"Sum of all discounts: ${total_discounts:.2f}")