# Initialisation

# Initialisation -> Relates to setting a particular data for an instance for a class
# Instantiation -> Is the creation of an instance of an object

class Dog:

    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"

fido = Dog("Fido", "Brown")

print(fido.name)
print(fido.colour)

# Initialising a class with class variables is good practice. It is possible to set variables, but it is not advised
