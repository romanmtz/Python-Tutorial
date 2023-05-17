#in programming languages there are basic types such as Integers, Strings, Boolean
#there are also some advanced types such as lists & dictionaries

#we can create new specialized types using classes

class Dog:
    def __init__(self, breed, sex): #this is how you initialize a constuctor more on that below
        self.breed = breed #self is a reference to the current object ex. in line 18 when i initialize a dog object, self refers to the current object being intiialized.
        self.sex = sex

    def sniff(self):
        print("*sniffs*")

    def bark(self):
        print("*barks*")


rex = Dog("german shepard", "female") #this is how you make a new Dog Object ;  note: an instance of variable that is associated with a class is called an object
buddy = Dog("pomeranian", "male") # if the object has a constructor you put the attributes as the arguments ex (breed, sex).

rex.sniff() #when you create a class you can add functions that apply to objects of that class

rex.cuteness = "very cute" # you can give attributes to an object like this anywhere in the program
print(rex.cuteness)

#however only the object that you specify will have this attribute
try:
    print(buddy.cuteness)
except AttributeError:
    print("this dog doesn't have a cuteness level")

#we can give every object in the dog class an attribute using constructers when creating the class line 7

print(rex.breed);
print(buddy.sex);

