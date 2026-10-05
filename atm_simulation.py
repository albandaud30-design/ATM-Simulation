class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited Rs. {amount:.2f}")
        else:
            print("Deposit amount must be greater than 0.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Successfully withdrawn Rs. {amount:.2f}")
class ATMController:
    def __init__(self):
        self.atm = ATM(10000)
    def show_menu(self):
        print("\n==============================")
        print("        ATM SIMULATION")
        print("==============================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==============================")
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                balance = self.atm.check_balance()
                print(f"Your current balance is Rs. {balance:.2f}")
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: Rs. "))
                    self.atm.deposit(amount)
                except ValueError:
                    print("Please enter a valid amount.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: Rs. "))
                    self.atm.withdraw(amount)
                except ValueError:
                    print("Please enter a valid amount.")
            elif choice == "4":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid choice. Please select 1-4.")
if __name__ == "__main__":
    controller = ATMController()
    controller.run()