# Lists are used to store multiple items in a single variable.

# List are created using a square bracket:
this_list = ["apple", "banana", "cherry"]
# print(this_list)

# Lists - ordered, changeable and allow duplicate values

# lists items are indexed, the first item has index[0], and second item has index[1] etc.

# Ordered - Order of Values cannot change, once value enter into a list, cannot change its order

# IF you add a new value to a list, it will be add / placed at the end of the list.

# Changeable - can change , add, and remove items in a list after it has been created.

# Allow duplicates :
# Since lists are indexed, lists can have items with the same values

list_items = ["apple","Banana", "cherry", "apple", "cherry"]
# print(list_items)


# List length
# Determine how many items a list has, use the len() function:

list_len = ["Rock", "triple H", "Undertaker", "John cena"]
# print(len(list_len))


# List items - Data types
# List items can be of any type, so

list_1 = ["apple", "Cherry", "Banana", "cherry", "apple", ""]

list_2 = [21,23,42,64,24,12,11,1,123,]

list_3 = [True, False, True, True, False]

print(list_1)
print(list_2)
print(list_3)


# A list can contain different data types:
list_diff_data = [True, 34, "Nikhil", "Male", 26]
print(list_diff_data)


# type of list
print(type(list_diff_data))


# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)