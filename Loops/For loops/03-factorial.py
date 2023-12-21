# Program to find the factorial of a number provided by the user.

# Change the value for a different result
# num = 9

# take input from the user
num_input = int(input("Enter a number: "))

factorial = 1

# to check if number negative,positive or zero
if num_input < 0:
  print("Sorry, factorial does not exist for negative numbers")
elif num_input == 0:
  print("The factorial of 0 is 1")
else:
  for i in range(1, num_input + 1):
    factorial = factorial * i
  print(f"Factorial of {num_input} is {factorial}")


# Explanation
  
# Iteration              Factorial * i (returned value)
# i = 1                   1 * 1 = 1
# i = 2                   1 * 2 = 2
# i = 3                   2 * 3 = 6
# i = 4                   6 * 4 = 24
# i = 5                  24 * 5 = 120 
# and cont..