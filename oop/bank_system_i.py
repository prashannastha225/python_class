from abc import ABC, abstractmethod

#Abstraction

class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def show_details(self, amount):
        pass



class SavingAccount(Bank):
    def __init__(self,name,inital_amount):
        self.name=name
        self.__initial_amount=inital_amount
        

    def deposit(self,amount):
        self._initial_amount=self._initial_amount+amount
        print(f"Your {amount} was deposited successfully")

    #polymorphism
    def withdraw(self,amount):
        if amount > self.__initial_amount:
            print("Insufficient Balance")
        else:
            self._initial_amount=self._initial_amount-amount
            print(f"Your {amount} was withdrawn successfully")

    def show_details(self):  
        print(f"Your current balance is {self.__initial_amount}")



class CurrentAccount(Bank):
    def _init_(self,name,inital_amount):
        self.name=name
        self.__initial_amount=inital_amount
        

    def deposit(self,amount):
        self._initial_amount=self._initial_amount+amount
        print(f"Your {amount} was deposited successfully")

    #polymorphism
    def withdraw(self,amount):
        if amount > self.__initial_amount+5000:
            print("Insufficient Balance")
        else:
            self._initial_amount=self._initial_amount-amount
            print(f"Your {amount} was withdrawn successfully")

    def show_details(self):
        print(f"YOur current balance is {self.__initial_amount}")


print("1.Saving Account\n2.Current Account\n")
acc_type = input("Choose 1 or 2: ")

if acc_type == "1":
    account = SavingAccount("Shiva",100000)
elif acc_type == "2":
    account = CurrentAccount("Shiva",100000)
else:
    print("Invalid choice")


print("Welcome to the Nabil Bank\n")

while True:

    print("1.Deposit\n2.Withdrawn\n3.Show_details\n4.Exit\n")

    choice=input("Enter your choice")

    match choice:
        case "1":
            amount=int(input("Enter your Amount to deposite"))
            account.deposit(amount)
            
        case "2":
            amount=int(input("Enter your Amount to withdraw"))
            account.withdraw(amount)
            
        case "3":
            account.show_details()
            
        case "4":
            print("Thank you for visting")
            break