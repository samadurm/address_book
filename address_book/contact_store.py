from abc import ABC, abstractmethod
from contact import Contact

class ContactStore(ABC):
    '''ContactStore is a class definition for keeping track of contacts.
    
    To update a contact, the contact must be removed then re-added.
    '''
    @abstractmethod
    def add(self, contact: Contact) -> int:
        pass

    @abstractmethod
    def remove(self, id: int):
        pass

    @abstractmethod
    def find(self, contact: Contact):
        pass