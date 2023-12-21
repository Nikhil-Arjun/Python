# Python Loops

# Python has two primitive loop commands:
# 1.While loops
# 2.for loops

# The While loop
# The while loop can execute a set of statements as long as a condition is true.

i = 1
while i < 6:
  print(i)
  i += 1

# remember to increment i, or else the loop will continue forever.

# while loop requires relevant variables to be ready, in this example we need to define an indexing variable i, which we set ot 1.
  

# The Break Statement
# The break statement we can stop the loop even if the while condition is true:
  
# Exit the loop when i is 3 ( i = 3)
  
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue statement
# The continue statement we can stop the current iteration 
  
# continue the loop when if i is 3:
  
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# Else statement
# The else statement we can run a block of code once when the condition is no longer is true:
  
i = 6
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")