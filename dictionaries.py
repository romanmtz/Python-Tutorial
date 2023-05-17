
#syntax
person = {
    "Name": "John Smith",
    "DOB": "April 18",
    "Age": "21"
}

print(person["Name"] + " " + person["Age"]) #how to extract definitions
print(person.get("name")) # doesn't return error/returns none if def does not exist
print(person.get("name","Roman")) # you can also supply a default value if def doesn't exist

#note: you can add new entries later person["new entry"] = "definition"