# positive integer greater than 1 which has no other factors expect 1 and the number itself -> prime number

# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print(f'Prime numbers between, {lower} and {upper}, are:')

for num in range(lower, upper+1):
  if num < 1:
    print("Enter a number within a range")
  elif num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break

    else:
        print(num)
        