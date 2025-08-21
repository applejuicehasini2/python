def calculate_due_amount(total_bill, amount_paid):
    due_amount = total_bill - amount_paid
    return due_amount

# Example usage
total_bill = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid: "))
due = calculate_due_amount(total_bill, amount_paid)

print(f"The due amount is: {due}")
