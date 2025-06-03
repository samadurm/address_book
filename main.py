from address_book.address_book import AddressBook
from address_book.contact import Contact

def print_contact(address_book: AddressBook):
    print(address_book)

def add_contact(address_book: AddressBook):
    while not (name := input("Enter name: ").strip()):
        print("A new contact needs at least a valid name")

    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = Contact(name=name, phone_number=phone, email=email, address=address)
    address_book.add(contact=contact)

def edit_contact(address_book: AddressBook):
    print('edit contact called')
    pass

def delete_contact(address_book: AddressBook):
    print('delete contact called')
    pass

def main():
    address_book = AddressBook()

    print('Address Book')

    command_map = {
        'p': print_contact,
        'a': add_contact,
        'e': edit_contact,
        'd': delete_contact
    }

    run = True
    while run:
        message = (f"Enter one of the following commands:\n"
                    f"- 'p': print current contact\n"
                    f"- 'a': add a new contact\n"
                    f"- 'e': edit a contact\n"
                    f"- 'd': delete a contact\n"
                    f"- 'q': quit\n"
        )

        lowercase_input = input(message).lower()
        if lowercase_input == 'q':
            break

        if func := command_map.get(lowercase_input):
            func(address_book=address_book)
        else:
            print('Invalid command.')
            


if __name__ == '__main__':
    main()