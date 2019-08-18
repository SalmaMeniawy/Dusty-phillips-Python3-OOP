class ContactList(list):
    def search(self,name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if contact.name == name:
                matching_contacts.append(contact)
        return matching_contacts

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

class Contact:
    all_contacts = ContactList()
    def __init__(self, name , email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
class Supplier(Contact):
    def order(self,order):
        print("If This were a real system we will send"
        "'{}' order to '{}'".format(order,self.name))
class Friend(Contact):
    def __init__(self,name,email,phone):
        super(Friend,self).__init__(name,email)
        self.phone = phone

