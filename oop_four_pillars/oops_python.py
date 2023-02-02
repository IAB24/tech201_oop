from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
         print("Ok let me get stretchy pants")
    def constrict(self):
         print("Squeeeze")
    def shed_skin(self):
         print("I'm growing now.")
    def climb(self):
         print("up we go")

peter = Python()

peter.hunt()
peter.shed_skin()

