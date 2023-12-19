# Program to swap two variables
# x = 5
# y = 10

# to take input form the user
x = int(input("Enter a 1st number of x variable: "))
y = int(input("Enter a 2nd number of y variable: "))

print(f'x: before {x}, y: after {y}')
# create a temp variable and swap the values
# temp = x
# x = y
# y = temp

# OR

x,y = y,x

print(f'x: after {x}, y: after {y}')