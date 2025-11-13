contacts = []

def Home():
    name=input("Enter a name: ")
    number=input("Enter a phone number: ")
    contacts.append(name)
    contacts.append(number)
    def save_cont():
        with open("contacts.txt", "a") as file:
            name,number = contacts
            file.write("| ")
            file.write(name+ "---")
            file.write(number)
            file.write(" |"+"\n")
    save_cont()

def read_contacts():
    with open("contacts.txt", "r") as file:
        contacts = file.read()
        print(contacts)

def delete_all():
    if input("Delete ALL contacts? Type 'yes' to confirm: ").strip().lower() == 'yes':
        open("contacts.txt", "w").close()
        print("Deleted all contacts.")
    else:
        print("Cancelled.")

print("\n Welcome to Contact Manager")
print("\n1. Add Contact\n2. View Contacts \n3. Delete All Contacts \n4. Exit Contact Manager ")
opt = input("\nChoose an option: ")

if opt == '1':
    Home()
elif opt == '2':
    read_contacts()
elif opt == '3':
    delete_all()
elif opt == '4':
    print("\nExiting Contact Manager \nHave a nice day!\n")