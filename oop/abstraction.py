from abc import ABC, abstractmethod

class BankApp(ABC):
    def database(self):
        print("database is connected")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def Mobile_UI(self):
        print("from mobile class")

    def security(self):
        print("this connection is secure")

obj = MobileApp()

obj.Mobile_UI()