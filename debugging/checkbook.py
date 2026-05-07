#!/usr/bin/python3
"""
Simple checkbook program.

This program allows a user to:
- Deposit money
- Withdraw money
- Check account balance
- Exit the application

The Checkbook class stores and manages the account balance.
"""


class Checkbook:
    """
    Represents a simple bank checkbook account.
    """

    def __init__(self):
        """
        Initialize the account with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount of money to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds exist.

        Args:
            amount (float): The amount of money to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop.

    Continuously prompts the user for actions until
    the user chooses to exit.
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? "
            "(deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)

        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()