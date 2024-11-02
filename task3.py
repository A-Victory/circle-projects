class Account:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Deposit amount must be positive.")

    def view_balance(self):
        print(f"Hello {self.name}, your current balance is: {self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter your name: ")
        while True:
            try:      
                initial_deposit = float(input("Enter initial deposit amount: "))
                if initial_deposit < 0:
                    print("Deposit amount cannot be negative. Please enter a positive amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        if name in self.accounts:
            print("Account with this name already exists!")
        else:
            self.accounts[name] = Account(name, initial_deposit)
            print("Account created successfully!")

    def deposit_money(self):
        name = input("Enter the name for the account: ")
        if name in self.accounts:
            amount = float(input("Enter amount to deposit: "))
            self.accounts[name].deposit(amount)
        else:
            print("Account not found.")

    def view_balance(self):
        name = input("Enter account name: ")
        if name in self.accounts:
            self.accounts[name].view_balance()
        else:
            print("Account not found.")

    def run(self):
        while True:
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.view_balance()
            elif choice == '4':
                print("Exiting the system. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()
