# Access items
# List items are indexed and you can access them by referring to the index numbers:

thislist = ['apple', 'banana', 'cherry']
# print(thislist[1])

# Negative indexing
# Negative indexing means start from the end of the list
# -1 -> last item

negv_list = ["Virat", "Rohit","Alex", 'Sachin']
# print(negv_list[-1])


# Range of indexes
# can specify a range of indexes by specifying where to start and where to end
# When specifying a range, the return value will be a new list the specified items.

range_list = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango"]
# print(range_list[2:5])

# print(range_list[:4])
print(range_list[2:])

# Range of Negative indexes
# Negative indexes if you want to start the search from the end of the list:

print(range_list[-4:-1])


# Check if item exists
# determine if a specified items is present in alist use the in keyword

check_list = ["Apple", "Banana", "Cheery"]
if "Mango" in check_list:
  print("Yes, Apple is in the fruits list")
elif "Banana" and "Cheery" in check_list:
  print("we are full now")
else:
  print("We don't neet to buy more")

# 