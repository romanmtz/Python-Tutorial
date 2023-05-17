names = ["John", "Amy", "Susan", "Steve"]
numbers = (1,2,3) #tuples are like lists but immutable [] = list () = tuple
matrix =[

    [1,2,4],
    [3,2,3],
    [1,5,3],
] # this is 2d array | indexes are referenced like this: matrix[row][column]

print(names[-1] + "\n") #in python you can use negative indexes -1 represents last item -2 second to last...
print(names[1:3])#you can also specify which indexes you want to print out

#array functions
names.append("Jerry")
names.insert(0,"Roman")

print(names)
print("in the array there are " + str(len(names)) + " indexes\n")


names.clear()
print(names)
print("in the array there are " + str(len(names)) + " indexes\n")



