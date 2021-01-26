"""
Using variables and types
"""

# TITLE: Section 1 - Variables & Types

# TODO: Section 1.1

# Assign an integer to the variable "bakers_dozen", then print it.

#bakers_dozen = 2
#print(bakers_dozen) 

# TODO: Section 1.2

# Assign an string to the variable "mary_had_a_little_lamb", then print it.

#mary_had_a_little_lamb = "Hello"
#`print(mary_had_a_little_lamb)

# TODO: Section 1.3
# Assign a float with 2 decimals to the variable "pi", then print it..

#pi = 3.1415
#print(pi)

# Assign True or False to the variable "the_dress_was_blue", then print it.

#the_dress_was_blue = True
#print(the_dress_was_blue) 

# TODO: Section 1.4
# Set 4 variables using only one line. The 4 variables should be made up of 1 integer, 1 string, 1
# float, and 1 boolean. Print each variable in its own print statement.

bakers_dozen, mary_had_a_little_lamb, pi, the_dress_was_blue = 2, "Hello", 3.1415, True

print(bakers_dozen)
print(mary_had_a_little_lamb)
print(pi)
print(the_dress_was_blue)

####################################################################################################

# TITLE: Section 2 - Type Function and Type Conversion

# TODO: Section 2.1

# Convert var2 to an integer so that we can print the sum of the two values.
var1 = 100
var2 = '200'
var3 = var1 + int(var2)

print(var3)

# TODO: Section 2.2

# Now try to convert var2 to a float and print the sum. What is the type of the sum?
var1 = 100
var2 = '200'
var3 = var1 + float(var2)

print(var3)