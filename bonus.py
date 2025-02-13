# Function to calculate the bonus
def calculate_bonus(salary, years_of_service):
    if years_of_service > 10:
        bonus = salary * 0.10
    elif 6 <= years_of_service <= 10:
        bonus = salary * 0.08
    else:
        bonus = salary * 0.05
    return bonus

# Input from the user
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))

# Calculate the bonus
bonus = calculate_bonus(salary, years_of_service)

# Print the result
print("Your net bonus is:", bonus)
