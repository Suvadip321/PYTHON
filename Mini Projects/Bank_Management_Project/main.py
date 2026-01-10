import json
import random
import string
from pathlib import Path

class Bank:
    __database = 'data.json'
    __data = []

    try:
        if Path(__database).exists():
            with open(__database, 'r') as db:
                __data = json.load(db)
        else:
            print("Database does not exist. Starting fresh...")
    except Exception as e:
        print("Error loading database:", e)

    @classmethod
    def __update(cls):
        """Write data to disk safely."""
        try:
            with open(cls.__database, 'w') as f:
                json.dump(cls.__data, f, indent=4)
        except Exception as e:
            print("Error writing database:", e)

    @classmethod
    def __gen_accNo(cls):
        """Generate a unique account number."""
        while True:
            alpha = ''.join(random.choices(string.ascii_uppercase, k=3))
            nums = ''.join(random.choices(string.digits, k=4))
            acc = alpha + nums

            if not any(u['accNo'] == acc for u in cls.__data):
                return acc

    @classmethod
    def __find_user(cls, accnum, pin):
        """Return user dict or None."""
        try:
            pin = int(pin)
        except:
            return None

        return next((u for u in cls.__data if u['accNo'] == accnum and u['pin'] == pin), None)

    def CreateAccount(self):
        name = input("Enter your name: ").strip()
        age = input("Enter your age: ").strip()
        email = input("Enter your email: ").strip()
        pin = input("Enter a four digit pin: ").strip()

        if not age.isdigit() or int(age) < 18:
            print("Invalid age. Must be 18 or above.")
            return

        if not pin.isdigit() or len(pin) != 4:
            print("PIN must be a 4-digit number.")
            return

        info = {
            'name': name,
            'age': int(age),
            'email': email,
            'pin': int(pin),
            'accNo': Bank.__gen_accNo(),
            'balance': 0
        }

        print("Account created successfully.")
        for k, v in info.items():
            print(f"{k}: {v}")
        print("Please note your account number.")

        Bank.__data.append(info)
        Bank.__update()

    def DepositMoney(self):
        accnum = input("Enter your account number: ").strip()
        pin = input("Enter your 4 digit pin: ").strip()

        userdata = Bank.__find_user(accnum, pin)
        if userdata is None:
            print("User not found.")
            return

        amount = input("Enter amount: ").strip()
        if not amount.isdigit():
            print("Amount must be numeric.")
            return

        amount = int(amount)
        if amount <= 0 or amount > 100000:
            print("Invalid amount.")
            return

        userdata['balance'] += amount
        Bank.__update()
        print(f"Deposited {amount}. Current balance: {userdata['balance']}")

    def WithdrawMoney(self):
        accnum = input("Enter your account number: ").strip()
        pin = input("Enter your 4 digit pin: ").strip()

        userdata = Bank.__find_user(accnum, pin)
        if userdata is None:
            print("User not found.")
            return

        amount = input("Enter amount: ").strip()
        if not amount.isdigit():
            print("Amount must be numeric.")
            return

        amount = int(amount)
        if amount <= 0 or amount > 100000:
            print("Invalid amount.")
            return

        if userdata['balance'] < amount:
            print("Insufficient balance.")
            return

        userdata['balance'] -= amount
        Bank.__update()
        print(f"Withdrawn {amount}. Current balance: {userdata['balance']}")

    def ShowDetails(self):
        accnum = input("Enter your account number: ").strip()
        pin = input("Enter your 4 digit pin: ").strip()

        userdata = Bank.__find_user(accnum, pin)
        if userdata is None:
            print("User not found.")
            return

        print("<Account Details>")
        for k, v in userdata.items():
            print(f"{k}: {v}")

    def UpdateAccount(self):
        accnum = input("Enter your account number: ").strip()
        pin = input("Enter your 4 digit pin: ").strip()

        userdata = Bank.__find_user(accnum, pin)
        if userdata is None:
            print("User not found.")
            return

        print("You can update: name, email, pin")
        print("Leave a field empty to keep it unchanged.")

        new_name = input("New name: ").strip()
        new_email = input("New email: ").strip()
        new_pin = input("New pin: ").strip()

        if new_pin:
            if not new_pin.isdigit() or len(new_pin) != 4:
                print("PIN must be a 4-digit number.")
                return
            userdata['pin'] = int(new_pin)

        if new_name:
            userdata['name'] = new_name

        if new_email:
            userdata['email'] = new_email

        Bank.__update()
        print("Details updated successfully.")

    def DeleteAccount(self):
        accnum = input("Enter your account number: ").strip()
        pin = input("Enter your 4 digit pin: ").strip()

        userdata = Bank.__find_user(accnum, pin)
        if userdata is None:
            print("User not found.")
            return

        choice = input("Press 'y' to confirm account deletion: ").strip().lower()
        if choice == 'y':
            Bank.__data.remove(userdata)
            Bank.__update()
            print("Account deleted successfully.")
        else:
            print("Account not deleted.")


def main():
    user = Bank()

    print("Press 0 to create an account")
    print("Press 1 to deposit money")
    print("Press 2 to withdraw money")
    print("Press 3 to see account details")
    print("Press 4 to update account details")
    print("Press 5 to delete account")

    try:
        resp = int(input("Enter your response: ").strip())
    except:
        print("Invalid input.")
        return

    if resp == 0:
        user.CreateAccount()
    elif resp == 1:
        user.DepositMoney()
    elif resp == 2:
        user.WithdrawMoney()
    elif resp == 3:
        user.ShowDetails()
    elif resp == 4:
        user.UpdateAccount()
    elif resp == 5:
        user.DeleteAccount()
    else:
        print("Please enter a valid response.")


if __name__ == '__main__':
    main()