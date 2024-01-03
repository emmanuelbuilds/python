# prints data type for each variable. Also note that variable are case-sensitive in python
x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as. both will be used as variable
x = 'John'
print(x)

# best practice is to use Pascal Case
MyVariableName = "John"
# pulling variables from a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variables
x = 5
y = 10
print(x + y)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# global variables have a function and a variable outside of it that gets plugged in
x = "awesome"
# variable is defined here and plugged into definition
def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
    global x
    x = "fantastic" # global determines what variable will be used for that specific function as x is already defined.

myfunc()

print("Python is " + x)