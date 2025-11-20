shopping_list = []

# adding items to the list
new_item = input("Add an item to the list:")
# shopping_list(new_item)

if new_item in shopping_list:
  print(f"{new_item} was not found in the list.")
else:
  shopping_list.append(new_item)
  print(f"{new_item} item was added to the list.")
  
  


#removing items from the list
remove_item = input("remove an item from the list:")
# shopping_list.remove(remove_item)

if remove_item in shopping_list:
    shopping_list.remove(remove_item)
    print(f"{remove_item} has been removed.")
else:
    print(f"{remove_item} was not found in the list.")

#printing items in the list
print("Current shopping list:", shopping_list)