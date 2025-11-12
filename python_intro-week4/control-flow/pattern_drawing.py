size = int(input("Enter the size of the pattern:."))

row = 0

# While loop controls the rows
while row < size:
    # For loop controls the columns (stars in each row)
    for col in range(size):
        print("*", end="")  # end="" keeps stars on same line
    print()  # move to the next line after one full row
    row += 1  # go to next row

# Ask for input → size = 4

# Set a variable row = 0 (start counting from 0)

# While row < size:

# Use a for loop to print size stars on the same line

# Print a newline (so it goes to the next row)

# Increase row by 1




# triangle_pattern.py
#each row number = number of stars in that row.
# Ask the user for size
size = int(input("Enter the size of the pattern: "))

# Start with the first row
row = 1

# While loop for rows
while row <= size:
    # For loop prints as many stars as the row number
    for col in range(row):
        print("*", end="")  # end="" keeps printing on same line
    print()  # move to next line after finishing one row
    row += 1  # go to the next row




# upside down
size = int(input("Enter the size of the pattern: "))
row = size
while row > 0:
    for col in range(row):
        print("*", end="")
    print()
    row -= 1