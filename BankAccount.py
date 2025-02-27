class BankAccount:
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}, New Balance: {self.balance}"

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}, New Balance: {self.balance}"

    def check_balance(self):
        return f"Current Balance: {self.balance}"

    def customer_details(self):
        return (f"Customer Name: {self.customer_name}\n"
                f"Account Number: {self.account_number}\n"
                f"Date of Opening: {self.date_of_opening}\n"
                f"Balance: {self.balance}")

# Example usage:
account = BankAccount("345267", "Badru", 5000, "2025-02-27")
print(account.deposit(2000))
print(account.withdraw(3000))
print(account.check_balance())
print(account.customer_details())
