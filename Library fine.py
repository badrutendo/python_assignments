from datetime import datetime

# Function to calculate fine
def calculate_fine(due_date, return_date):
    # Convert string dates to datetime objects
    due_date = datetime.strptime(due_date, "%Y-%m-%d")
    return_date = datetime.strptime(return_date, "%Y-%m-%d")

    # Calculate days overdue
    days_overdue = (return_date - due_date).days

    # Determine fine rate
    if days_overdue <= 0:
        fine_rate = 0
    elif days_overdue <= 7:
        fine_rate = 20
    elif days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100

    # Calculate total fine
    fine_amount = days_overdue * fine_rate if days_overdue > 0 else 0

    return days_overdue, fine_rate, fine_amount

# Get inputs from the user
book_id = input("Enter Book ID: ")
due_date = input("Enter Due Date (YYYY-MM-DD): ")
return_date = input("Enter Return Date (YYYY-MM-DD): ")

# Compute fine
days_overdue, fine_rate, fine_amount = calculate_fine(due_date, return_date)

# Display output
print("\nLibrary Fine Details")
print(f"Book ID: {book_id}")
print(f"Due Date: {due_date}")
print(f"Return Date: {return_date}")
print(f"Days Overdue: {days_overdue}")
print(f"Fine Rate: Ksh {fine_rate} per day")
print(f"Total Fine Amount: Ksh {fine_amount}")
