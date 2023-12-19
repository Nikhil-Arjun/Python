# program to find the area of triangle

a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a + b + c) /2
# print(f'Semi perimeter is {s}')

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print(f'The area of the triangle is {area} ')


# OR

base = float(input("Enter a value of base: "))
height = float(input("Enter a value of height: "))

area_of_triangle = (1/2) * base * height
print(f'The area of the triangle is {area_of_triangle}')