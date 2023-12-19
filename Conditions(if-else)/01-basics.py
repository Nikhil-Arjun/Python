# Python If...else

# Python Conditions and If statement
# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less Than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to : a >= b

# these condition can be used in several ways, most commonly in "If statement" and loops.

# IF statement
# value_a = 33
# value_b = 200

# if value_b > value_a:
#   print("B is greater than a")


# Elif statement
# The elif keyword is python's way of saying "If the previous conditions were not true, then try this conditions"
  
# value_of_a = 33
# value_of_b = 33

# if value_of_b > value_of_a :
#   print("b is greater than a")
# elif value_of_a == value_of_b :
#   print("Both a and b values are equal")


# Else statement
# The else keyword catches anything which isn't caught by the preceding conditions.
  
value_of_a = 200
value_of_b = 33

if value_of_b > value_of_a:
  print("B is greater than A")
elif value_of_a == value_of_b:
  print("A and B are equal")
else:
  print("A is greater than B")