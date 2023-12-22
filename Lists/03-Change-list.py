# Python - Change List items

# Change item value
# To change the value of a specific item, refer to the index number:

change_list = ["apple", "banana" ,"cherry"]
change_list[1] = "blackcurrent"
# print(change_list)

# Change a range of item values
# To change the values of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

change_item = ["apple", "banana", "cherry", "orange", "kiwi","Mango"]
change_item[1:3] = ["blackcurrent", "watermelon"]
# print(change_item)


# Insert Items
# Without replacing any of the existing values, can use the insert() method.

# The insert() method inserts an item at the specified index:

insert_item = ["Apple", "Banana", "Cherry"]
insert_item.insert(2, "watermelon")
print(insert_item)
# 