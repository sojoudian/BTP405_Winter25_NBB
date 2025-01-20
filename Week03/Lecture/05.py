# A Function for Calculating the Areaof Shapes

from typing import Union

# Type hint for a function that calculates 
# The area of a rectangle or a circle
def calculate_area(shape: str, size: Union[float, int]) -> float:
    if shape == "rectangle":
        # For calculate rectangle area, the `size` is asumed to e the side length
        return size * size
    elif shape == "circle":
        from math import pi
        return pi * size * size
    else:
        raise ValueError("Unsupported shape type")
        #return f"Unsupported shape type"
#try:
#   block of code    
#except XXXX:
#   error 1
#except YYYYY:
#   error 2


print()
print(calculate_area("rectangle", 5.0))
print()
print()
print(calculate_area("circle", 3))
print(calculate_area("circle", "1"))