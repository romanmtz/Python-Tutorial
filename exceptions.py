#note: when a program exits it returns an exit code 0 if it succeeds, or another number if there is an error.
#exceptions can catch these errors instead of quitting the program altogether

try:
    #if the user tries to use a string as an argument this line will fail and return ValueError
    num = int(input("enter a number but whatever you do not a string: "))
    print(num)

except ValueError:
    print("caught the error! You cannot enter that!")

#note: you can have more than 1 exception in a try-except construct
#there are many different types of errors which can be found in the terminal when the program exits