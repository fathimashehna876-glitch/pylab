class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        """Constructor to initialize a bank account."""
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the bank account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraw money from the bank account."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_account_info(self):
        """Display account details."""
        print("\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print("----------------------------")


# Main program
if __name__ == "__main__":
    print("=== Welcome to Python Bank ===")
    
    # Getting user inputs dynamically
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Savings/Current): ")
    balance = float(input("Enter Initial Balance: "))

    # Create BankAccount object
    account = BankAccount(acc_no, name, acc_type, balance)

    # Menu-driven operations
    while True:
        print("\nChoose an operation:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Display Account Info")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == '3':
            account.display_account_info()

        elif choice == '4':
            print(f"Current Balance: {account.balance}")

        elif choice == '5':
            print("Thank you for banking with us! Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
