"""Program to represent Bank Accounts and functionalities performed on the account using Class."""


class BankAccount:
    """class for all Bank Accounts."""

    # all characteristics of a bank acoount
    number = 00000000  # Account number
    holder = []  # array of all account holders
    ac_type = " "  # account type(Checking/Saving)
    balance = 0  # balance in the account

    def __init__(self, number, holder, ac_type, balance):
        """Constructor which takes values for all account characteristics."""
        self.number, self.ac_type, self.balance = number, ac_type, balance
        self.holder.append(holder)

    def retrieve_account_number(self):
        """Function to retreive Account Number."""
        return self.number

    def retrieve_account_holder(self):
        """Function to retreive all Account Holders."""
        return self.holder

    def retrieve_account_balance(self):
        """Function to retreive Account Balance."""
        return self.balance

    def retrieve_account_type(self):
        """Function to retreive Account Type."""
        return self.ac_type

    def deposit(self, amount):
        """Function to deposit money given the bank account and the amount to add in it."""
        self.balance = self.balance + amount  # deposit amount

    def withdraw(self, amount):
        """Function to withdraw money given the bank account and the amount to remove from it."""
        # the withdraw amount has to be less than the balance in that account
        if amount <= self.balance:
            self.balance = self.balance - amount  # withdraw amount
            return 1  # 1 is returned as a flag for withdraw success
        else:
            # if withdraw amount is greater than balance, 0 is returned as a flag for failure
            return 0

    def add_holder(self, holder):
        """Function to add account holder."""
        self.holder.append(holder)  # append the new holder to the current array of account holders


# Main Function Starts here
if __name__ == '__main__':
    # creation of object by passing the values to the constructor for initialization
    greg = BankAccount(12345678, "Gregory House", "Checking", 1000)
    # retrieve all characteristics and store them in temperory variables
    number, holder = greg.retrieve_account_number(), greg.retrieve_account_holder()
    ac_type, balance = greg.retrieve_account_type(), greg.retrieve_account_balance()
    print("Current State for {} is: \n Account Number:{} \n Account Type:{} \n Balance:{}\n".format(
        holder[0], number, ac_type, balance))

    greg.deposit(100)  # deposit 100$ in greg's account
    number, holder = greg.retrieve_account_number(), greg.retrieve_account_holder()
    ac_type, balance = greg.retrieve_account_type(), greg.retrieve_account_balance()
    # retrieve and print the new characteristics of his account
    print ("Account State after Deposit for {} is:  \n Account Number: {}\n Account Type: {}"
        " \n Balance: {} \n"
        .format(holder[0], number, ac_type, balance))

    success = greg.withdraw(2500)  # withdraw 2500$ from greg's account
    # print new characteristics if withdraw is successful
    if success == 1:
   		number, holder = greg.retrieve_account_number(), greg.retrieve_account_holder()
   		ac_type, balance = greg.retrieve_account_type(), greg.retrieve_account_balance()
        print ("Account State after Withdrawal for {} is:"
            "\n Account Number: {}\n Account Type: {}\n Balance: {}\n"
            .format(holder[0], number, ac_type, balance))

    # if withdraw failed, print an error message
    else:
        print("Withdraw transaction of 2500$ not successful due to Insufficient funds\n"
        "Hence state of the account remains same for {}:"
        "\n Account Number: {}\n Account Type: {}\n Balance: {}\n".format(
            holder[0], number, ac_type, balance))

    # add account holder
    greg.add_holder(" Mrs. Gregory House")
    number, holder = greg.retrieve_account_number(), greg.retrieve_account_holder()
    ac_type, balance = greg.retrieve_account_type(), greg.retrieve_account_balance()
    # print new characteristics
    print ("Account holder added for\n Account Number: {} \n Account Type: {}, \n Balance: {} \n"
    "The updated holders are:{}, {}".format(number, ac_type, balance, holder[0], holder[1]))

"""OUTPUT
Current State for Gregory House is:
 Account Number:12345678
 Account Type:Checking
 Balance:1000

Account State after Deposit for Gregory House is:
 Account Number: 12345678
 Account Type: Checking
 Balance: 1100

Withdraw transaction of 2500$ not successful due to Insufficient funds
Hence state of the account remains same for Gregory House:
 Account Number: 12345678
 Account Type: Checking
 Balance: 1100

Account holder added for
 Account Number: 12345678
 Account Type: Checking,
 Balance: 1100
The updated holders are:Gregory House,  Mrs. Gregory House
"""
