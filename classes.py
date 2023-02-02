# Object-Oriented Programming (OOP)

# Everything in OOP is an object and objects are modelled against real world objects.

# Classes are the templates we use to create objects
# Classes are a way of bringing both data and functionality of our code together.

# Create a class

class Dog:

    animal_kind = "Canine" # class variable

    def bark(self): #method
        return "woof"

#self - I'm referring to the current class.
# print(Dog.animal_kind)
# print(Dog.bark())

# Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
fido.animal_kind = "Big Dog"

print(fido.animal_kind)
print(lassie.animal_kind)
# Output = Big Dog
#          Canine
# Benefit is you can be specific about objects without affecting other objects.

Dog.animal_kind = "Dolphin" #Overwrite the template

# The dog's can still access their method
print(fido.bark()) # woof
