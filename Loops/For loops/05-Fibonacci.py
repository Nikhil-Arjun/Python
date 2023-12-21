# A Fibinacci sequence is the integer sequence of 0,1,1,2,3,5,8,13,21,........

# First two term are 0 and 1.
# n1 = 0
# n2 = 1

# All other terms are obtained by adding the preceding two terms.

num_terms = int(input("How many terms ? : "))

# first two tems
n1 = 0
n2 = 1
count = 0


# check if the number of terms is valid or not
if num_terms <= 0:
  print("Please enter a positive integer")
# if there is only one term, return n1
elif num_terms == 1:
  print("Fibonacci sequence upto", num_terms, ":")
  print(n1)
# generate Fibonacci sequence
else:
  print("Fibonacci Sequence: ")
  while count < num_terms:
    print(n1)
    n_add = n1 + n2
    n1 = n2
    n2 = n_add
    # count += 1

