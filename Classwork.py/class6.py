
grocery_list = ["milk", "bread", "eggs"]


def add_item(item):
    grocery_list.append(item)
    print(f'"{item}" added to grocery list.')

def remove_last_item():
    if grocery_list:
        removed_item = grocery_list.pop()
        print(f'"{removed_item}" removed from grocery list.')
    else:
        print("Grocery list is already empty.")


display_item = lambda item: print(f"Item: {item}")


def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

# -------------------------------
# Example Usage:

# Display initial list
print("Initial Grocery List:")
for item in grocery_list:
    display_item(item)

# Add an item
add_item("cheese")

# Remove last item
remove_last_item()

# Display updated list
print("\nUpdated Grocery List:")
for item in grocery_list:
    display_item(item)

# Count total characters
total_chars = count_characters(grocery_list)
print(f"\nTotal characters in all items: {total_chars}")
