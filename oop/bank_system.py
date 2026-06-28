class Banksys:
    def __init__(self, name, initial_amount):
        self.name = name
        self.initial_amount = initial_amount


    def deposit(self, amount):
        self.initial_amount = self.initial_amount + amount
        print(f"your {amount} has been deposited")

    def withdraw(self, amount):
        self.initial_amount = self.initial_amount - amount
        print(f"your {amount} has been withdrawn")

    def show_details(self):
        pass

acc_1 = Banksys("Ram Bahadur", 100)

print("Welcome to Nabil bank")

while True:

    print("1.deposit\n2.withdraw\n3.account_info\n4.Exit")

    choice = input("state your choice(1,2,3,4):")

    match choice:
        case "1":
            amount = int(input("Enter your amount to deposit: "))
            acc_1.deposit(amount)
            continue

        case "2":
            amount = int(input("Enter your amount to withdraw: "))
            acc_1.withdraw(amount)
            continue

        case "3":
            acc_1.show_details()
            continue

        case "4":
            print("Thank You for using the banking system")
            break