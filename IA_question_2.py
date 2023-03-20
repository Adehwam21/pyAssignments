from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self):
        self._owner = None
        self._balance = 0.0

    def deposit(self):
      
      amount = int(input("Enter amount to deposit: "))
      self._balance = self._balance + amount
      return self._balance
   
    def withdraw(self):
      pass
   

class CheckingAccount(BankAccount):
   
    def setOwner(self, acc_number: str) :
      self._owner = acc_number

    def getOwner(self) -> str:
      return self._owner
   
    def withdraw(self):
      amount = int(input("Enter amount to withdraw: "))
      transaction_fee = .5

      if self._balance < amount:
         print("Insufficient balance")
      else:
         self._balance = self._balance - (amount + transaction_fee)
         return print(f"Withdrawal Successful!\nDear {self.getOwner()}, you withdrew GHc{amount} from your Checking Account.\nYour current balance is : GHc{self._balance}. Transaction fee was {transaction_fee}")
         

class SavingsAccount(BankAccount):
   
    def setOwner(self, acc_number: str) :
      self._owner = acc_number
    def getOwner(self) -> str:
      return self._owner
   
    def withdraw(self):
      amount = int(input("Enter amount to withdraw: "))

      if self._balance < amount:
         print("Insufficient balance")
      else:
         self._balance = self._balance - amount
         return print(f"Withdrawal Successful!\nDear {self.getOwner()}, you withdrew GHc{amount} from your Savings Account.\nYour current balance is : GHc{self._balance}.")
      
if __name__ == "__main__":
   acc1 = CheckingAccount()
   acc2 = SavingsAccount()

   acc1.setOwner("Aaron")
   acc2.setOwner("Benedicta")

   acc1.deposit()
   acc2.deposit()

   acc1.withdraw()
   acc2.withdraw()
