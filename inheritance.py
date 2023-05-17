#Using inheritance a class can 'inherit' the functions of another class

class Food:
    def eat(self):
        print("*eat*")

class Bread(Food): #this is the syntax for inheritance: the class you inherit from goes within parenthesis.
    pass #pass just tells the interpreter to skip the line.

loaf = Bread()
loaf.eat()