import utils.math_operations as math_operations

data = 5

# Using the functions as if they were instance methods
squared = math_operations.square(data)
cubed = math_operations.cube(data)
doubled = math_operations.double(data)
tripled = math_operations.triple(data)

print("Original:", data)
print("Squared:", squared)
print("Cubed:", cubed)
print("Doubled:", doubled)
print("Tripled:", tripled)
