coordinates = (1,2,3)
#without unpacking
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

#with unpacking
x,y,z = coordinates # the elements of the list are unpacked left to right

#both lines of code achieve the same goal

print(f'{x},{y},{z}')