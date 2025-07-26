# Requirements:
# Core Functionality:

# Your script should start with an empty list named shopping_list.
# Implement functionality to add items to the list, remove items, and display the current list.
# User Interface:

# Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
# For adding items, prompt the user for the item name and append it to shopping_list.
# For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
# To view the list, print each item in shopping_list to the console.
# Ensure your script handles invalid menu choices gracefully.


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

        if choice == '1':
            add_item = input('Enter the item to add: ')
            shopping_list.append(add_item)
            print('item added to shopping list')
        elif choice == '2':
            remove_item = input('Enter the item to remove: ')
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print('item removed from shopping list')
            else:
                print('Item not found in shopping list')
        elif choice == '3':
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
