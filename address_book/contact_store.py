from abc import ABC, abstractmethod
from address_book.contact import Contact

class ContactStore(ABC):
    '''ContactStore is a class definition for keeping track of contacts.
    
    To update a contact, the contact must be removed then re-added.'''
    @abstractmethod
    def add(self, contact: Contact) -> int:
        pass

    @abstractmethod
    def remove(self, id: int):
        pass

    @abstractmethod
    def find(self, key) -> Contact:
        '''Returns a contact that corresponds with the given key.

        For a quick lookup, use the id returned from add() as the key. Else use the full name.'''
        pass

class InMemoryContactStore(ContactStore):
    '''InMemoryContactStore is a ContactStore that is kept in memory.
    
    Use when persisting contacts is not needed between sessions (such as for testing).'''
    
    class IdGenerator:
        def __init__(self):
            self._id_counter = 0
        
        def next(self) -> int:
            id = self._id_counter
            self._id_counter += 1
            return id
    
    def __init__(self):
        self._items = dict()
        self._id_generator = self.IdGenerator()

    def add(self, contact: Contact) -> int:
        id = self._id_generator.next()
        self._items[id] = contact
        return id
    
    def remove(self, id: int):
        if id in self._items:
            del self._items[id]

    def find(self, key) -> Contact:
        if isinstance(key, int):
            if key in self._items:
                return self._items[key]
            return None
        elif isinstance(key, str):
            for contact in self._items.values():
                if key == contact.name():
                    return contact
            return None
        return None