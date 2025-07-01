import json
import os
import uuid

FILE_NAME = 'data.json'

# 1. View all data
def view_data():
    if not os.path.exists(FILE_NAME):
        print(" Error: File does not exist.")
        return

    with open(FILE_NAME, 'r') as file:
        try:
            data = json.load(file)
            if not data:
                print(" No records found.")
            else:
                for item in data:
                    print(f" ID: {item['id']}")
                    print(f" Name: {item['name']}")
                    print(f" Age: {item['age']}")
                    print("-" * 30)
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")


# 2. Create new data
def create_data(name, age):
    data = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                pass  # empty or invalid JSON

    for item in data:
        if item['name'].lower() == name.lower():
            print("Error: Duplicate name not allowed.")
            return

    new_entry = {
        "id": str(uuid.uuid4()),
        "name": name,
        "age": age
    }
    data.append(new_entry)

    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

    print("Data created successfully.")


# 3. Edit existing data by ID
def edit_data(id, new_name, new_age):
    if not os.path.exists(FILE_NAME):
        print("Error: File does not exist.")
        return

    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    found = False
    for item in data:
        if item['id'] == id:
            item['name'] = new_name
            item['age'] = new_age
            found = True
            break

    if found:
        with open(FILE_NAME, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data updated successfully.")
    else:
        print("Error: ID not found.")


# 4. Delete data by ID
def delete_data(id):
    if not os.path.exists(FILE_NAME):
        print("Error: File does not exist.")
        return

    with open(FILE_NAME, 'r') as file:
        data = json.load(file)

    new_data = [item for item in data if item['id'] != id]

    if len(new_data) == len(data):
        print("Error: ID not found.")
    else:
        with open(FILE_NAME, 'w') as file:
            json.dump(new_data, file, indent=4)
        print("🗑️ Data deleted successfully.")


# 💬 Main Menu
while True:
    print("\n===== MENU =====")
    print("1. View Data")
    print("2. Create Data")
    print("3. Edit Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_data()

    elif choice == "2":
        name = input("Enter name: ")
        age = input("Enter age: ")
        if age.isdigit():
            create_data(name, int(age))
        else:
            print("Error: Age must be a number.")

    elif choice == "3":
        id = input("Enter ID to edit: ")
        new_name = input("Enter new name: ")
        new_age = input("Enter new age: ")
        if new_age.isdigit():
            edit_data(id, new_name, int(new_age))
        else:
            print("Error: Age must be a number.")

    elif choice == "4":
        id = input("Enter ID to delete: ")
        delete_data(id)

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")
1