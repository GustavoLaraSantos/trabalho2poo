from Items import Items

def main():
    item_system = Items("test_items.json")

    # Create items
    try:
        item_system.create_item("Apples", 10)
        item_system.create_item("Bananas", 5)
        print("Items created successfully.")
    except ValueError as e:
        print(e)

    # List items
    print("Listing all items:")
    for item in item_system.list_items():
        print(item)

    # Read specific item
    try:
        print("Reading item 'Apples':")
        print(item_system.read_item("Apples"))
    except ValueError as e:
        print(e)

    # Update item
    try:
        print("Updating 'Apples' quantity to 20.")
        item_system.update_item("Apples", 20)
        print(item_system.read_item("Apples"))
    except ValueError as e:
        print(e)

    # Delete item
    try:
        print("Deleting item 'Bananas'.")
        item_system.delete_item("Bananas")
        print("Item deleted.")
    except ValueError as e:
        print(e)

    # List items after deletion
    print("Listing all items after deletion:")
    for item in item_system.list_items():
        print(item)

main()
