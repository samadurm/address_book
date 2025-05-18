class Contact:
    '''Represents a contact with name, phone number, email, and physical address.

    All parameters must be strings.'''
    
    def __init__(self, name: str, phone_number: str, email: str, address: str):
        if not all(isinstance(arg, str) for arg in [name, phone_number, email, address]):
            raise TypeError('All parameters must be strings')
        
        self._name = name
        self._phone_number = phone_number
        self._email = email
        self._address = address

    def name(self):
        return self._name
    
    def phone_number(self):
        return self._phone_number
    
    def email(self):
        return self._email
    
    def address(self):
        return self._address
    
    def __repr__(self):
        return (f"Contact(name={self._name!r}, phone_number={self._phone_number!r}, "
            f"email={self._email!r}, address={self._address!r})")
