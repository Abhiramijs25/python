class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance

    def show_info(self):
        print(f"Account Holder: {self._name}")
        print(f"Balance: ₹{self._balance:.2f}")


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05 

class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02 


savings = SavingsAccount("Ravi", 10000)
current = CurrentAccount("Anjali", 15000)

print("---- Savings Account ----")
savings.show_info()
print(f"Interest: ₹{savings.calculate_interest():.2f}\n")

print("---- Current Account ----")
current.show_info()
print(f"Interest: ₹{current.calculate_interest():.2f}\n")

total_balance = savings + current
print("---- Total Balance ----")
print(f"Total Balance (Ravi + Anjali): ₹{total_balance:.2f}")
