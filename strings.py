# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

#! String Concatinate
name = "John"
age = 24
city = "New York"

print("Hello, " + name + "!") #concatinate
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

#! String Formatting
# a.) Using Arguments by position
print("Hello, my name is {} and I am {} years old. I live in {}".format(name, age, city))
print("Hello, my name is {1} and I am {2} years old. I live in {0}".format(name, age, city))
# b.) Using Arguments by name
print("Hello, my name is {name} and I am {age} years old.".format(name=name, age=age))
# c.) F-Strings (Python 3.6+)
print(f"Hello, my name is {name} and I am {age} years old. I live in {city}")


#! Get Length 
#len(stingVariable) returns the length
testString = "This is a test string"
print(len(testString))

#! String Methods
testString = "This is a test string"
# capitalize() - Converts the first character to upper case
# upper() - Converts a string into upper case
# lower() - Converts a string into lower case
# swapcase() - Swaps cases, lower case becomes upper case and vice versa
# replace() - Replaces a string with another string
# strip() - Removes any whitespace from the beginning or the end similar to "trim()" 
# count() - Returns the number of times a specific value occurs in a string
# startswith() - Returns true if the string starts with the specified value
# endswith() - Returns true if the string ends with the specified value
# split() - Splits the string into substrings
# find() - Searches the string for a specified value and returns the position of where it was found
# isalnum() - Returns True if all the characters are alphanumeric
# isalpha() - Returns True if all the characters are in the alphabet
# isnumeric() - Returns True if all the characters are numeric



print(testString.strip().split(" "))
print(testString.count("t"))
print(testString.strip().replace("t", "g"))





