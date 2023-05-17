def function_name(): #creating function
    print("Hello World!")

def function_with_parameter(param): #creating function with 1 parameter
    print(f"Hello {param}!")

def function_with_parameters(param1, param2): #creating function with multiple parameters
    print(f"Hello {param2}, {param1}!")

def function_that_returns_a_value(param1,param2):
    return param1 + param2 #by defualt if there is no return statent python retunrs None

print("normal function calling:")
function_name() #calling function

print("\ncalling function with parameter:")
function_with_parameter(input("What is your name? ")) #you call a function that requires a parameter like this

print("\ncalling functioin with two parameters (positional arguments):")
function_with_parameters("John", "Smith") #you enter multiple arguments separeted by a comma ; position matters

#keyword arguments are used when you don't want to worry about the position of the arguments ie. positional arguments
print("\ncalling function with two parameters (keyword arguments):")
function_with_parameters(param2="Smith",param1="John") 

#note: Parameters are the placeholders we define in the function while arguments is the data we give to the function
print("\nprinting what a function that returns a value returns:")
print(function_that_returns_a_value(5,3))# we are printin what the function returns which should be the sum of param1 and param2