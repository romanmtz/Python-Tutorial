#you can make a string that spans multiple lines using triple quotes
multi_line_string = """
Multi Line String Example:
Line 1
Line 2
Line 3
"""

print(multi_line_string)

#python strings have indexes
print("String Indexing Examples: ")
string = "Python Tutorial"
print(string) #print entire string note: string[:] has the same effect
print(string[0]) #print first index
print(string[-1]) # -1 represents the last index in the string
print(string[0:-2]) #prints 0 -> -2 excluding -2 note: 0 is assumed if not starting index is chosen

print("String Formatting Examples: ")

string1 = "Roman"
string2 = "Basketball"

normal_string = string1 + " likes " + string2 + "."
print(normal_string)

#formatted strings are prefixed with an f'' 
#variables are surrounded by {}
formated_string = f'{string1} likes {string2}.' 
print(formated_string)

# string methods
# len(string) gives length of string note:general purpose function not exclusive to strings
# string.upper() / string.lower() converts all char in string to uppercase or lowercase
# string.find(string tofind) returns index int of the first occurence of the string to find: returns -1 when there is no occurence
# string.replace(string tofind, string toreplace) like find but also replaces with string to replace
# you can also use the in operator for a boolean expression ex. "P" in "Python" = True