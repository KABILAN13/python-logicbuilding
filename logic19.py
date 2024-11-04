number = int(input("Enter a number: "))

# Get the unit digit
unit_digit = number % 10

# Get the tenth digit
tenth_digit = (number // 10) % 10

# Calculate the sum
sum_digits = unit_digit + tenth_digit

print("Sum of tenth and unit digits:", sum_digits)
