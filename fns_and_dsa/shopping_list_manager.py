# shopping_list = []

# # adding items to the list
# new_item = input("Add an item to the list:")
# # shopping_list(new_item)

# if new_item in shopping_list:
#   print(f"{new_item} was not found in the list.")
# else:
#   shopping_list.append(new_item)
#   print(f"{new_item} item was added to the list.")
  
  


# #removing items from the list
# remove_item = input("remove an item from the list:")
# # shopping_list.remove(remove_item)

# if remove_item in shopping_list:
#     shopping_list.remove(remove_item)
#     print(f"{remove_item} has been removed.")
# else:
#     print(f"{remove_item} was not found in the list.")

# #printing items in the list
# print("Current shopping list:", shopping_list)

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':  # Add Item
            new_item = input("Enter the item to add: ")
            if new_item in shopping_list:
                print(f"{new_item} is already in the list.")
            else:
                shopping_list.append(new_item)
                print(f"{new_item} item was added to the list.")

        elif choice == '2':  # Remove Item
            remove_item = input("Enter the item to remove: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"{remove_item} has been removed.")
            else:
                print(f"{remove_item} was not found in the list.")

        elif choice == '3':  # View List
            if shopping_list:
                print("Current shopping list:")
                for item in shopping_list:
                    print(item)
            else:
                print("Shopping list is empty.")

        elif choice == '4':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
