# If/ Else conditions are used to decide to do something based on something being true or false
#! Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
#! Logical operators (&& , ||, !) => (and, or, not)  - Used to combine conditional statements

def learnCondtionals(x, y):
    if x == y:
        print(f"{x} is equal to {y}")
    elif x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    elif x >= y:
        print(f"{x} is greater than or equal to {y}")
    elif x <= y:
        print(f"{x} is less than or equal to {y}")
    else:
        print(f"{x} is less than {y}")
    return

def learnConditionals2(x, y):
    if x == y:
        print(f"{x} is equal to {y}")
        return
    if x > y:
        print(f"{x} is greater than {y}")
        return
    if x < y:
        print(f"{x} is less than {y}")
        return
    if x >= y:
        print(f"{x} is greater than or equal to {y}")
        return
    if x <= y:
        print(f"{x} is less than or equal to {y}")
        return
    else:
        print(f"{x} is less than {y}")
    return

def learnConditionals3(x):
    if x > 2 and x < 10:
        print(f"{x} lies between 2 and 10")
    else:
        print(f"{x} is out of range")
    return
 
learnCondtionals(10, 10)
learnConditionals2(10, 10)
learnConditionals3(5)
learnConditionals3(15)
#! Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object
numbs = [1, 2, 3, 4, 5]

def isXPresent(x, myList):
    if x in myList:
        print(f"{x} is present in the list")
    else:
        print(f"{x} is absent in the list")
    return

def isXNotPresent(x, myList):
    if x not in myList:
        print(f"{x} is absent in the list")
    else:
        print(f"{x} is present in the list")
    return

isXPresent(5, numbs)
isXNotPresent(5, numbs)



#! Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

def IdentityOperators(x, y):
    if x is y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is not equal to {y}")
    return

def IdentityOperators2(x, y):
    if x is not y:
        print(f"{x} is not equal to {y}")
    else:
        print(f"{x} is equal to {y}")
    return

IdentityOperators(10, 10)
IdentityOperators2(10, 20)
#! Bitwise Operators (&, |, ^, ~, <<, >>) - Used to perform bit operations

