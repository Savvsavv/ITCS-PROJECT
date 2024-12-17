def Code_Challenge16():
    # create a function that will breakdown a filipino denomination and then print it
    # Create a python program that can create banking accounts, with the ff. information initial deposit, name 
    #user can deposit, withdraw, and every deposit program should be able to deposit, current balance
    #program will only terminate if user choose to terminate the program

    # Banking System Program
    print ("\n Made by: Savannah Mari De Mesa")

    # Banking System Functions

    def breakdown_denominations(amount):
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        breakdown = {}
        for deno in denominations:
            if amount >= deno:
                breakdown[deno] = amount // deno
                amount %= deno
        return breakdown

    # Function to display denomination breakdown
    def print_breakdown(amount):
        print(f"\nBreakdown of PHP {amount}:")
        breakdown = breakdown_denominations(amount)
        for deno, count in breakdown.items():
            print(f"PHP {deno}: {count} piece")

    accounts = {}

    def create_account():
        name = input("Enter your name: ").strip()

        while True:

            try:
                initial_deposit = float(input("Enter initial deposit: "))
                if initial_deposit < 0:
                    print("Initial deposit cannot be negative. Try again.")
                    continue
                accounts[name] = initial_deposit
                print(f"Account created successfully for {name} with balance PHP {initial_deposit:.2f}!")
                print_breakdown(initial_deposit)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def deposit(name):
        if name in accounts:

            while True:

                try:
                    amount = float(input("Enter amount to deposit: "))
                    if amount < 0:
                        print("Amount cannot be negative. Try again.")
                        continue
                    accounts[name] += amount
                    print(f"Deposited PHP {amount:.2f}. Current balance: PHP {accounts[name]:.2f}")
                    print_breakdown(amount)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        else:
            print(f"Account with name {name} does not exist.")

    def withdraw(name):
        if name in accounts:

            while True:

                try:
                    amount = float(input("Enter amount to withdraw: "))
                    if amount < 0:
                        print("Amount cannot be negative. Try again.")
                        continue
                    if amount > accounts[name]:
                        print("Insufficient funds. Try a smaller amount.")
                        continue
                    accounts[name] -= amount
                    print(f"Withdrew PHP {amount:.2f}. Current balance: PHP {accounts[name]:.2f}")
                    print_breakdown(amount)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
        else:
            print(f"Account with name {name} does not exist.")

    def view_balance(name):
        if name in accounts:
            print(f"{name}'s Current Balance: PHP {accounts[name]:.2f}")
        else:
            print(f"Account with name {name} does not exist.")

    # Main Program
    while True:
        print("\n--- Banking System ---")
        print("\nPlease Select An Option")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Exit")
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                create_account()
            elif choice == 2:
                name = input("Enter your name: ")
                deposit(name)
            elif choice == 3:
                name = input("Enter your name: ")
                withdraw(name)
            elif choice == 4:
                name = input("Enter your name: ")
                view_balance(name)
            elif choice == 5:
                print("Thank you for using the Banking System. Goodbye and See You Again!\nProgram Terminated")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Please enter a valid number.")


Code_Challenge16()
