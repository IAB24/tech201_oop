from animal import Animal #caps let's pyhton know you want class

class Reptile(Animal):  #Reptile inherits from animal variables. Can also add reptile specific things

    def __init__(self):
        super().__init__() #inheriting from animal. Initialize animal first before reptile.
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None


    def seek_heat(self):
        print("It's chilly outside, where is the sun")

    def hunt(self):
        print("Wait, wait, wait... pounce")

    def use_venom(self):
        print("If I have got it, I am going to use it")

    def attract_through_scent(self):
        print("Time to spray some eut de toilette")

jeremy_the_reptile = Reptile()

jeremy_the_reptile.tetrapod
jeremy_the_reptile.hunt()
jeremy_the_reptile.procreate()
jeremy_the_reptile.move()