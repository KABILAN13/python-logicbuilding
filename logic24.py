s = "3a2b1c"  # Example input
result = ""
i = 0

while i < len(s):
    # Initialize a variable to store the number
    num = 0
    
    # Loop through the digits to form the number
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])  # Handle multiple digits
        i += 1
    
    # Now append the alphabet `num` times to the result
    if i < len(s) and s[i].isalpha():
        result += s[i] * num
        i += 1  # Move to the next character

# Print the expanded result
print(result)
