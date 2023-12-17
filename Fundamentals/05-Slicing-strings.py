# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and end index, separated by a colon, to return a part of the string.


# String is same like array, index start from 0.
b_string = "Rockstar Games"
# print(b_string[2:11])

# Slice from the start
# By leaving out the start index, the range will start at the first character

sample_string = "Rockstar Games"
# print(sample_string[:6])


# Slice to the end
# by leaving out the end index, the range will go to the end:

samp_string = "Bruce Wayne"
# print(samp_string[4:])

# Negative index
# Use negative indexes to start the slice from the end of the string:

b = "Hello World"
# print(b[::-1])

print(b[-5:-2])

