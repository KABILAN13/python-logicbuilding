# Input two numbers
a = 30
b = 40

# Implement Euclidean algorithm directly
while b != 0:
    a, b = b, a % b

# After the loop, 'a' will hold the GCD
print(f"GCD is {a}")
