# Booleans represent one of two values: True or False. 

# When you compare two values, the expression is evaluated and python returns the boolean answer:

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# When you run a condition in an if statement, Python returns True and false:

# value_a = 33
# value_b = 200

# if value_a > value_b:
#   print("Value of A is greater than Value B")
# else:
#   print("Value of A is less than Value B")

# Evaluate values and variables
# The bool() function allows yoi to evaluate any value, and give you True and false in return

# print(bool("Hello"))
# print(bool(15))

x = "Hello"
y = "15"

# print(bool(x))
# print(bool(y))


# Function can return a boolean
def myFunction():
  return "John Wick"

# print(myFunction())

# can execute code based on the boolean answer of a function:

if myFunction():
  print("YES!")
else:
  print("No!")