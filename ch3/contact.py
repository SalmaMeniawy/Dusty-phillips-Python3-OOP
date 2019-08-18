class ContactList(list):
    def search(self,name):
        '''Return all contacts that contain the search value
        in their name.'''
        matching_contacts = []
        for contact in self:
            if contact.name == name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = []
    def __init__(self, name , email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
class Supplier(Contact):
    def order(self,order):
        print("If This were a real system we will send"
        "'{}' order to '{}'".format(order,self.name))
