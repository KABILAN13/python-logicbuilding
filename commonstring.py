# Input parsing
S1 = input().strip()  # First string
S2 = input().strip()  # Second string

# Convert strings to sets to get unique characters
set_S1 = set(S1)
set_S2 = set(S2)

# Find common characters using intersection
common_characters = set_S1.intersection(set_S2)

# Output the count of common characters
print(len(common_characters))
