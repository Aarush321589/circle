import math

def find_circumference(radius):
    """
    This function returns the circumference of a circle
    given its radius.
    Formula: C = 2 * π * r
    """
    if radius < 0:
        return "Radius cannot be negative."
    circumference = 2 * math.pi * radius
    return circumference

# Example usage
r = float(input("Enter the radius of the circle: "))
result = find_circumference(r)
print(f"The circumference of the circle is: {result}")
