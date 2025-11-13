class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance  # Account balance
        self.total_fees = 0  # Total fees ever deducted due to overdrafts

    def deposit(self, amount):
        """Deposits the amount into the account."""
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal 
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """
        if amount > 0:
            self.balance -= amount
            if self.balance < 0:
                self.total_fees += 5  # Deduct a penalty fee of 5 dollars
                self.balance -= 5  # Apply the penalty fee

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.total_fees


# TEST CASE

account1 = BankAccount(20)
account1.deposit(10)

account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)

account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)

account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)

account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)

account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)

account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)

account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)

account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)

account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)

account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)

# Print the final balances and fees for both accounts
print(account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees())



class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance  # Account balance
        self.total_fees = 0  # Total fees ever deducted due to overdrafts

    def deposit(self, amount):
        """Deposits the amount into the account."""
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal 
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """
        if amount > 0:
            self.balance -= amount
            if self.balance < 0:
                self.total_fees += 5  # Deduct a penalty fee of 5 dollars
                self.balance -= 5  # Apply the penalty fee

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.total_fees


# TEST CASE
my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)

# Print the balance and total fees deducted
print(my_account.get_balance(), my_account.get_fees())
