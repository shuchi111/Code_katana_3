class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        self.transactions = []

    def withdraw(self, amount):
        potential_balance = self.balance - amount
        if potential_balance < 1000:
            fee = amount * 0.05
            total_deduction = amount + fee
            if total_deduction > self.balance:
                print("Insufficient funds for withdrawal and fees.")
                return False
            else:
                self.balance -= total_deduction
                self.transactions.append({'type': 'withdrawal', 'amount': amount, 'fee': fee})
        else:
            self.balance -= amount
            self.transactions.append({'type': 'withdrawal', 'amount': amount, 'fee': 0})

        print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
        return True

# Example of using the BankAccount class
account = BankAccount('123456789', 1500)
account.withdraw(600) 
account.withdraw(1000) 