"""
polymorphism: single interface but many implementations

types:
1. overriding
2. overloading (not supported in python)
3. duck polymorphism
"""

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# A = Animal()
# A.sound()

D = Dog()
D.sound()