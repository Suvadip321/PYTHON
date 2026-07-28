"""
LESSON: Encapsulation & Properties
──────────────────────────────────
# Encapsulation: Hiding internal data and requiring methods to access it
# Protected (_var): A warning that a variable is meant for internal use only
# Private (__var): Python actively renames the variable to hide it (Name Mangling)
# @property: Decorator that lets you access a method like a normal variable
"""

class BankAccount:
  def __init__(self, account_number, balance):
    self.account_type = "Savings"          # public attribute (accessible)
    self._account_number = account_number  # protected attribute (accessible, but not recommended)
    self.__balance = balance               # private attribute (not accessible)

  @property
  def balance(self):
    """Read-only access to balance (GETTER)"""
    return self.__balance
    
  @balance.setter
  def balance(self, new_balance):
    """Safe modification of balance (SETTER)"""
    if new_balance >= 0:
      self.__balance = new_balance
    else:
      print("Balance cannot be negative!")
      
  def deposit(self, amount):
    if(amount > 0):
      self.__balance += amount
      print(f"Deposited {amount}. Balance: {self.__balance}")
    else:
      print("Invalid deposit amount!")
      
  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      print(f"Withdrawn {amount}. Balance: {self.__balance}")
    else:
      print("Invalid withdraw amount!")


# create account
acc = BankAccount("12345", 1000)

# public attribute: directly accessible
print(acc.account_type)

# protected attribute: accessible but not recommended
print(acc._account_number)

# private attribute: not directly accessible
# print(acc.__balance)

# modify and access safely using methods
acc.deposit(500)
acc.withdraw(750)
print(acc.balance)

# using the @property SETTER directly
print("\n--- Using the Setter ---")
acc.balance = 5000  # This safely calls the @balance.setter method!
print("New Balance:", acc.balance)

acc.balance = -100  # This will trigger our setter's validation!
