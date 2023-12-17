# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# print('hello')
# print("hello")

# Assign String to a variable
a = "Hello"
# print(a)

# Multiple string
multiple_string = """ 
lorem ipsum dolor sit amet, consectetur adipiscing elit"""

# print(multiple_string)


# Strings are Arrays
# Strings in python are arrays of bytes representing unicode characters.

string_array = "Hello World!"
# print(string_array[4])

# Looping through a string
for x in "mango":
  print(x)

# String length
String_length = "Hello World!"
print(len(String_length))

# Check string
# To check if a certain phrase or char is present in a string, can use the keyword in

text = "the best things in life are free!"
print("free" in text)

# Use it in an if statement:
text_1 = "The another best things in life are memories"
if "best" in text_1:
  print("Yes, 'Free' is present.")


# Check if Not
  
text_2 = "The best thing in life is time!"
print("Expensive" not in text_2)

# use it in an if statement:
text_3 = "The another best thing in life is money."
if "money" not in text_3:
  print("Money, most 'important' thing in a life")