# TODO:
# Define a function called "area_rectangle()" that will find the area of a rectangle. This
# function should take two parameters, "length" and "width". Use a conditional to determine if the
# area of the rectangle is greater than 10 square units. If the condition is true,
# print("This is a large rectangle."). If not, then print("This is not a large rectangle.")

# After defining the function, test your function by calling it and passing 2 arguments of your choice.

# Hint: The area of a rectangle is equal to its length times its width.

def area_rectangle(length, width):
    dim = length * width
    if (dim > 10):
        print("This is a large rectangle.")
    else:
        print("This is not a large rectangle.")

area_rectangle(2,10)