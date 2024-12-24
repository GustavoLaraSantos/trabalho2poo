from Items import Items

def main():
    item_system = Items("test_items.json")

    # Create items
    response = item_system.create_item("Apples", 10)
    print(response)
    response = item_system.create_item("Bananas", 5)
    print(response)
    response = item_system.create_item("Apples", 10)
    print(response)
    print("Items created successfully.")

    # List items
    print("Listing all items:")
    response = item_system.list_items()
    print(response)

    # Read specific item
    print("Reading item 'Apples':")
    response = item_system.read_item("Apples")
    print(response)
    response = item_system.read_item("Oranges")
    print(response)

    # Update item
    print("Updating 'Apples' quantity to 20.")
    response = item_system.update_item("Apples", 20)
    print(response)
    response = item_system.update_item("Oranges", 20)
    print(response)
    print(item_system.read_item("Apples"))

    # Delete item
    print("Deleting item 'Bananas'.")
    response = item_system.delete_item("Bananas")
    print(response)
    response = item_system.delete_item("Oranges")
    print(response)

    # List items after deletion
    print("Listing all items after deletion:")
    response = item_system.list_items()
    print(response)

main()
