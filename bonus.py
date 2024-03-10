class BankAccount:
    def _init_(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
        self.transactions = []

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        

        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(-amount)  
     
            if self.balance < 1000:
                # Apply penalty of 5%
                penalty = 0.05 * amount
                self.balance -= penalty
                self.transactions.append(-penalty) 
            return f"Withdrawal of ${amount} successful. Current balance: ${self.balance}"
        else:
            return "Insufficient funds"

# Example :
'''''
account = BankAccount("123456789", 1500)
print(account.withdraw(500))  
print(account.withdraw(700))  
print(account.withdraw(400))  '''