# Input strings
S1 = "delicacy"
S2 = "celibacy"

# Initialize count for common characters
count = 0

# Convert the second string to a list to allow removal of characters
S2_list = list(S2)

# Loop through each character in the first string
for char in S1:
    # Check if the character exists in the second string
    if char in S2_list:
        # Increment the count
        count += 1
        # Remove the character from the second string list to prevent recounting
        S2_list.remove(char)

# Print the total number of common characters
print(count)
