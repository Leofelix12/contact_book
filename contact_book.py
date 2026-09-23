running = True

contacts = []

try:
    with open("contacts.txt", "r") as f:
        for line in f:
            contacts.append(line.strip())
except FileNotFoundError:
    pass

while running:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("You want to add contact.")
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts.append(name + "," + phone)
        with open("contacts.txt", "w") as f:
            for contact in contacts:
                f.write(contact + "\n")
        print("contact added.")
        
    elif choice == "2":
        print("You want to view contacts.")
        print(contacts)
        
        
    elif choice == "3":
        print("Goodbye.")
        running = False
        
    else:
        print("Invalid choice. Try again.")
