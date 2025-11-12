rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks
  
# myrows = 5
# for n in range(1, myrows + 1):
#    for p in range(1, n + 1):
#      print(" ", "*", " ", end="" )
#      print() 
myrows = 5

for n in range(1, myrows + 1):
    # print spaces
    for p in range(1, myrows - n + 1):
        print(" ", end="")

    # print stars
    for p in range(1, 2 * n):
        print("*", end="")

    # move to the next line after each row
    print()

     