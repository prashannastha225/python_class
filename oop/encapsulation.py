"""
encapsulation: binding of data, methods and protect things from direct access

specifier:
1. Public
2. protected: use single underscore
3. private: use double underscore
"""

# class User:
#     def __init__(self, name, ID, password):
#         self.name = name
#         self.ID = ID
#         self.__password = password # making a private property

#     # def get__password(self):
#     #     return self.__password

#     def get_name(self):
#         return(self.__password)
    
#     def set_name(self,__password):
#         self.__password

# a = User("ram", "7", "ram123")
# print(a.name)
# print(a.__password)

# a.set_name,"shyam123"

# ----------------------------------------------------
# ----------------------------------------------------


# class user:
#     def __init__(self, _name, password):
#         self._name = _name
#         self.password = password

# class student(user):
#     def show(self):
#         print(self._name)

# c = student("ram", "ram124")
# c.show()
# print(c._name)