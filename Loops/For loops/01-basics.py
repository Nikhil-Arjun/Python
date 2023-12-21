
# Python for loop

# for loop is used for iterating over a sequence (list, tuple, dictionary, set, string)

fruits = ["Apple", "Banana", "cherry", "Pamogrende", "grapes", "Sweet limes"]

# for fruit in fruits:
  # print(fruit)

# The for loop does not require an indexing variables to set beforehand.
  

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
  
# for x in "banana":
  # print(x)


# The break statement
# With the break statement can stop before it has looped through all the items.
  
Batsman = ["Virat ", "Sachin", "MS Dhoni", "Rohit", "SKY"]
for batter in Batsman:
  if batter == "MS Dhoni":
    break
  # print(batter)



# The Continue statement
# The continue statement can stop the current iteration of the loop, and continue with the next:
  
Batsman = ["Virat ", "Sachin", "MS Dhoni", "Rohit", "SKY"]
for batter in Batsman:
  if batter == "Rohit":
    continue
  # print(batter)


# The range() function
# To loop through a set of code a specified number of times, can use the range() function.
  
# The range() function returns a sequence of numbers, starting form  0 by default, and increments by 1 (by default) and ends at a specified numbers.
  
for x in range(6):
  print(x)

# Range - Start from 0 and ends with num-1
# 0 - default
# can specify the starting value by adding a parameter: range(2,6)
  
# range : start - 2 and Ends - 5
  
# range default increment is 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)

# for x in range(2, 30, 3):
  # print(x)


# Nested loops

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the 'outer loop'
  

adj = ["red", "big", "Tasty"]
fruits = ["Apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)