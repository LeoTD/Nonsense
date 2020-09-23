
# Zip function!
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

# Using the tuple() function to display a readable version of the result:

print(tuple(x))

def foo():
    """
    Function docstring!
    Args:
        - yolo:
        - swag:
        - money:
    """
    print(420)

foo()

squares = []
for x in range(1, 11):
 square = x**2
 squares.append(square)

 squares = [ x**2 for x in range(1, 11) ]
