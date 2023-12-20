# Using if...elif...else

num = float(input("Enter a number: "))

# if num > 0:
#   print("Number is positive number")
# elif num == 0:
#   print("Number is neither positive nor negative")
# else:
#   print("Number is negative Number")



# Using Nested if

if num >= 0:
  if num == 0:
    print("Zero")
  else:
    print("Positive number")
else:
  print("Negative number")
