import unittest
from address_book.contact_store import InMemoryContactStore
from address_book.contact import Contact

class InMemoryContactStoreTest(unittest.TestCase):
    def test_add(self):
        c1 = Contact(name="Bob Smith", phone_number="0000000000", email="bobsmith@gmail.com", address="123 Something Way, Columbus, Ohio")
        c2 = Contact(name="Dana Jones", phone_number="0000000000", email="dj@gmail.com", address="123 Something Way, Columbus, Ohio")

        store = InMemoryContactStore()
        bob_id = store.add(c1)
        dana_id = store.add(c2)

        self.assertEqual(c2, store.find(dana_id), "Could not find Dana in store")
        self.assertEqual(c1, store.find(bob_id), "Could not find Bob in store")

    def test_remove(self):
        c1 = Contact(name="Bob Smith", phone_number="0000000000", email="bobsmith@gmail.com", address="123 Something Way, Columbus, Ohio")
        c2 = Contact(name="Dana Jones", phone_number="0000000000", email="dj@gmail.com", address="123 Something Way, Columbus, Ohio")

        store = InMemoryContactStore()

        # ensure that removing on empty doesnt throw
        store.remove(0)
        store.remove(-1)

        bob_id = store.add(c1)
        dana_id = store.add(c2)

        store.remove(bob_id)
        self.assertIsNone(store.find(bob_id), "Bob should have been removed from the store")
        
        store.remove(dana_id)
        self.assertIsNone(store.find(dana_id), "Dana should have been removed from the store")

    def test_find_empty(self):
        store = InMemoryContactStore()
        self.assertIsNone(store.find(0), "Find on an empty store should return nothing")

    def test_find_by_name(self):
        c1 = Contact(name="Bob Smith", phone_number="0000000000", email="bobsmith@gmail.com", address="123 Something Way, Columbus, Ohio")
        c2 = Contact(name="Dana Jones", phone_number="0000000000", email="dj@gmail.com", address="123 Something Way, Columbus, Ohio")

        store = InMemoryContactStore()
        store.add(c1)
        store.add(c2)

        self.assertEqual(c1, store.find("Bob Smith"), "Should have been able to find Bob Smith by full name")
        self.assertEqual(c2, store.find("Dana Jones"), "Should have been able to find Dana Jones by full name")