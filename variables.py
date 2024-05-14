# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
print("Hello World") #simple print
name = "Yash"
print(name) # print variable
print(name, "Hello") # print multiple


#! DataTypes in Python.. 

myInt = 7
_myFloat = 7.5
myStr = "test"
myBool = True

print(myInt, myBool, myStr, _myFloat)

#! Multiple Assignments of variable in Python 
intTest = 8
floatTest = 8.5
stringTest = "testing"
boolTest = False
tuplTest = (1, 10, 30, "john", 'doe', True);
listTest =  [1, 10, 30, "john", 'doe', True];
dictTest =  {1, 10, 30, "john", 'doe', True};
print(intTest, floatTest, stringTest, boolTest, tuplTest[4], listTest, dictTest)
# tuplTest[4] = "jane"
listTest[4] = "jane"
print(tuplTest, listTest)
#! Basic math
b = 10
a = b + 15.5
b = 15
print(a, b)

#! Check data-type of a variable
print(type(a))
print(type(floatTest))
print(type(stringTest))
print(type(boolTest))

#! Type Casting in Python
temp = str(int(a))
print(temp, type(temp),a , type(a))

