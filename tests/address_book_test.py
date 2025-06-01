import unittest

from address_book.address_book import AddressBook
from address_book.contact import Contact

class AddressBookTest(unittest.TestCase):
    def test_add_and_remove(self):
    
        c1 = Contact(name="Bob Smith", phone_number="123-456-8910", email="bob_smith@gmail.com", address="123 Test Way, Test, CO")
        c2 = Contact(name="Lara Thompson", phone_number="123-456-1122", email="lara_t@gmail.com", address="456 Test Way, Test, CO")
        c3 = Contact(name="Alice Jones", phone_number="707-124-0819", email="alicej@yahoo.com", address="789 Test Way, Test, CO")

        address_book = AddressBook()
        key1 = address_book.add(c1)
        self.assertEqual(c1, address_book.find(key1), "First contact was not added")

        address_book.add(c2)
        self.assertEqual(c2, address_book.find(c2.name()), "Second contact was not added")

        address_book.add(c3)
        self.assertEqual(c3, address_book.find(c3.name()), "Third contact was not added")

        # Test both remove using both id and name
        address_book.remove(c2.name())
        self.assertIsNone(address_book.find(c2.name()), "Second contact should have been removed")

        address_book.remove(c1.name())
        self.assertIsNone(address_book.find(key1), "First contact should have been removed")

        address_book.remove(c3.name())
        self.assertIsNone(address_book.find(c3.name()), "Third contact should have been removed")


    def test_string_representation(self):
        c1 = Contact(name="Bob Smith", phone_number="123-456-8910", email="bob_smith@gmail.com", address="123 Test Way, Test, CO")
        c2 = Contact(name="Lara Thompson", phone_number="123-456-1122", email="lara_t@gmail.com", address="456 Test Way, Test, CO")

        address_book = AddressBook()
        address_book.add(c1)
        address_book.add(c2)

        str_rep = str(address_book)
        self.assertTrue(str(c1) in str_rep, 
                        "Contact 1 should be contained in the string representation")
        self.assertTrue(str(c2) in str_rep, 
                "Contact 2 should be contained in the string representation")

