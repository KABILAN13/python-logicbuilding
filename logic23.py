# Input string
s = input("Enter a string: ")

# Find the index of the first underscore
underscore_index = s.find('_')

# If an underscore is found, reverse the part before it and keep the rest unchanged
if underscore_index != -1:
    result = s[:underscore_index][::-1]+s[underscore_index:] # Reverse up to the first underscore and append the rest

print(result)

