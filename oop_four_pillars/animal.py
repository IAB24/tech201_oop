# Abstraction

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in one breath out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Find a mate")

    def move(self):
        print("Onwards and upwards")

cat = Animal()
cat.breathe()
# user doesn't need to know logic. Just need to know how to use the method. Only know what you need to know.

