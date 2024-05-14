# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces
def hello():
    print("Hello")
hello()

def helloUser(user="admin"):
    print(f"Hello {user}")

def getSum(num1, num2):
    total = num1 + num2
    return total
sum  = getSum(2, 3)
print(sum)
helloUser("Yash")

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2: num1 + num2
print(getSum(3, 4))

hellUser = lambda user="admin": print(f"Hello {user}")
hellUser("John")