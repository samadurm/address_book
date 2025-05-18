import unittest
from address_book.contact import Contact

class ContactTest(unittest.TestCase):
    def test_create_contact_all_empty(self):
        Contact("", "", "", "")

    def test_create_contact(self):
        name = "Bob Smith"
        phone = "000-000-0000"
        email = "bobsmith@gmail.com"
        address = "123 Test Way, Test City, Test State"
        c = Contact(name=name, phone_number=phone, email=email, address=address)

        self.assertEqual(name, c.name())
        self.assertEqual(phone, c.phone_number())
        self.assertEqual(email, c.email())
        self.assertEqual(address, c.address())

    def test_non_string_parameter_throws_exception(self):
        name = "Bob Smith"
        phone = 1234567890
        email = "bobsmith@gmail.com"
        address = "123 Test Way, Test City, Test State"
        with self.assertRaises(TypeError):
            Contact(name=name, phone_number=phone, email=email, address=address)


if __name__ == '__main__':
    unittest.main()