class Warrior:
    def attack(self):
        print("Warrior swings a sword!")

class Mage(Warrior):
    def attack(self):
        print("Mage casts a fireball!")

class Archer(Warrior):
    def attack(self):
        print("Archer shoots an arrow!")

party = Warrior() and Archer()
print(party.attack())