# Program to check if a number is prime or not.

# num = 29

# to take input from the user 
# num_input = int(input("Enter a number: "))

# # define a flag variable
# flag = False

# if num_input == 1:
#   print(num_input, "is not a prime number")

# elif num_input > 1:
#   # check for factors
#   for i in range(2, num_input):
#     # print(i)
#     if(num_input % i) == 0:
#       # if factor is found, set flag as a true value
#       flag = True
#       # Break out of loop
#       break

  
#   # check if flag is True
#   if flag:
#     print(num_input, "is not a prime number")
#   else:
#     print(num_input, "is a prime number")



# More easy way:

num = 407

# Take input from the user
num = int(input("Enter a number: "))

if num == 1:
  print(f'{num} is not a prime number')
elif num > 1:
  # check for factors
  for i in range(2, num):
    if(num % i) == 0:
      print(f'{num} is not a prime number')
      print(f'{i} * {num // i} is {num}')
      break
  
  else:
    print(f'{num} is a prime number')


# if input number is less than 
# or equal to 1, it is not prime
else:
  print(f'{num} is not a prime number')