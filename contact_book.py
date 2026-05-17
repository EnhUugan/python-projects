def menu():
    print("")
    print("█▓▒­░⡷⠂ CONTACT BOOK ⠐⢾░▒▓█")
    print("")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. View all contacts")
    print("5. Quit")
    print("")

#Memory
contacts = {
    
}

#Code
while True:
    menu()
    try:
        choice = int(input("Choose your option: "))
        if choice == 5:
            print("Are you sure?")
            quit_confirm = str(input("Yes or No: "))
            if quit_confirm == "Yes":
                print("Thank you!!")
                break
            else:
                print("Wrong Input!")
                menu()
        elif choice == 1:
            print("")
            print("***NEW CONTACT***")
            while True:
                name = str(input("Please type their name: "))
                phone = str(input("Please enter their phone number: "))
                print("")
                new_confirm = str(input(f"Type Yes if their name is {name} and phone number is {phone}: "))
                if new_confirm == "Yes":
                    contacts[name] = phone
                    print("Contact Saved!")
                    break
                else:
                    print("")
                    continue
        elif choice == 2:
            print("")
            print("***SEARCH***")
            search = str(input("Enter their name: "))
            phone = contacts.get(search)
            if phone:
                print(f"{search}'s phone number is {phone}")
            else:
                print("Not Found!!")
        elif choice == 3:
            print("")
            print("***DELETE***")
            delete = str(input("What name should i remove?: "))
            if delete in contacts:
                contacts.pop(delete)
                print(f"{delete} got Removed from your contacts!!")
            else:
                print(f"Couldn't find {delete} from your contacts!")
        elif choice == 4:
            print("")
            if len(contacts) == 0 :
                print("EMPTY")
            else:
                print("***CONTACTS***")
                print("")
                for name, phone in contacts.items():
                    print(f"Name: {name}")
                    print(f"Phone Number: {phone}")
                    print("")
        
    except:
        print("Wrong Input!!")
        



