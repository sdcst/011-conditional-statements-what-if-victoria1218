#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""


a = float(input("Enter one side: "))
b = float(input("Enter a second side: "))
c = float(input("Enter third side: "))
if a > b and a > c:
    h = round(a)
    d = round(b)
    e = round(c)
if b > a and b > c:
    h = round(b)
    d = round(a)
    e = round(c)
if c > a and c > b:
    h = round(c)
    d = round(a)
    e = round(b)
if (d**2+e**2) > (h**2):
    print("that is an acute triangle")
elif (d**2+e**2) < (h**2):
    print("that is an obtuse triangle")
else:
    print("that is a right triangle")
