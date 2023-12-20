# Program to find the largest number among the three input numbers.

# number_1 = 34
# number_2 = 98
# number_3 = 12

# also you can take three numbers from user
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
num_3 = float(input("Enter third number: "))

# to check num_1 is greater or not
if (num_1 >= num_2) and (num_1 >= num_3):
  largest = num_1

# to check num_2 is greater or not
elif (num_2 >= num_1) and (num_2 >= num_3):
  largest = num_2

# if both conditions are failed, remaining num_3 is largest number.
else:
  largest = num_3

print(f'The largest number is', largest)