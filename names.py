# Initialize an empty list to store names
names_list = []

# Ask the user how many names they want to enter
num_names = int(input("How many names would you like to enter? "))

# Loop to collect names one by one
for i in range(num_names):
    name = input("Enter name " + str(i + 1) + ": ").strip()  # Remove extra spaces
    names_list.append(name)

# Remove duplicates by converting to a set, then back to a list
updated_names = list(set(names_list))

# Sort the list alphabetically
updated_names.sort()

# Display the sorted list
print("\nSorted names (duplicates removed):")
for name in updated_names:
    print(name)

# Print the total number of names entered initially
print("\nTotal number of names entered: " + str(num_names))
