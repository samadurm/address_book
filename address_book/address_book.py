from . import contact_store
from .contact import Contact

class AddressBook:
    def __init__(self):
        self.contact_store = contact_store.InMemoryContactStore()

    def add(self, contact: Contact) -> int:
        return self.contact_store.add(contact)        

    def remove(self, name: str):
        id = self.contact_store.find_id(name)
        if id is not None:
            self.contact_store.remove(id)

    def find(self, key) -> Contact:
        '''Performs a lookup on internal store using the provided key.

        The key can be the integer id associated with the contact, or the contact name.'''
        
        return self.contact_store.find(key)
    
    def __str__(self):
        return str(self.contact_store)