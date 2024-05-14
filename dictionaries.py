# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#! creating a dictionary
# a.) general method
person = {
    "first_name": "Yash", 
    "last_name": "Sharma", 
    "age": 30,
    "test": {
        "a": "b"
    }
}
# b.) using dict constructor
fruits1 = dict(first_name="Yash", last_name="Sharma", age=30)
# print(person)

#! Accessing Values
# print(person["first_name"]) # Using Square brackets
# print(person.get("last_name")) # Using .get method

#! Add item(i.e., key : value tuple pair) to dictionary
person["city"] = "New York"
person["number"] = "+91 999 999 9999"
# print(person)

#! get keys
# print(person.keys())

#! get values
# print(person.values())

#! get items(i.e, key : value tuple pair)
# print(person.items())


#! Make a copy of a dictionary
person2 = person.copy()
person2["first_name"] = "John"
# print(person)
# print(person2)

#! Remove item from dictionary
del person["city"]
del(person["number"])
print(person)

#! Clear dictionary
person.clear()
print(person)


#! Delete dictionary
del person
# print(person)

#! get Length
print(len(person2)) 
