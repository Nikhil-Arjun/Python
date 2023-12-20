# Program to check if year is a leap year or not.

year = 2000

# To get year(int input) from the user
year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):
  print(f'{year} is a leap year')

# not divided by 100 means not a century year
elif (year % 4 == 0) and (year % 100 != 0):
  print(f'{year} is a leap year')

# if not divided by both 400 (century year) and 4 (not century year)
# year is not a leap year
else:
  print(f'{year} is not a leap year')