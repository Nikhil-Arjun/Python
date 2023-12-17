# String format
# We cannot combine or concar strings and numbers

# can combine strings and numbers by using the format() method!.

# The Format() method takes the passed arguments, formats them, and palces them in the string where the placeholders {} are:

# person_name = input("Enter your name: ")
# person_age = int(input("Enter your age: "));

# using f-string(recommended)
# result = (f'My name is {person_name}, and I am {person_age}')

# result = "My name is {}, and I am {} "

# print(result.format(person_name, person_age))

# The format() methods takes unlimited numbers of arguments, and placed into the respective string where the placeholders.

quantity = 3
item_no = 567
price_item = 49.58
# customer_order = "I want {} pieces of items {} for {} dollars."

# print(customer_order.format(quantity,item_no,price_item))

# or

# you can use index numbers{0} to be sure the arguments are placed in the correct placeholders

customer_order = "I want to pay {2} dollars for {0} pieces of items {1}."

print(customer_order.format(quantity,item_no, price_item))