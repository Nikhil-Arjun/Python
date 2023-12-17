# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.

# Upper-Case
# The upper() method returns the string in upper case:
string_upper = "John Wick"
print(string_upper.upper())


# Lower-case
# The lower() method returns the string in lower case:
lower_string = "HackerRank"
print(lower_string.lower())


# Remove Whitespace
# Whitespace is space before and/or after the actual text, and very often you want to remove this space.

# The strip() method removes any whitespace from the beginning and end:
strip_string = " RakaZone Gaming!  "
print(strip_string.strip())


# Replace String
# The replace() method replaces a string with another string.
replace_string = "Virat kohli"
print(replace_string.replace("V", "k"))


# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.
split_string = "Royal, Challenger, Banglore"
print(split_string.split(","))