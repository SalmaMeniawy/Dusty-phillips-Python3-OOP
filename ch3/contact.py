class AddressHolder:
    def __init__(self,street='' , city='' ,state='' , code='',**kwargs):
        super(AddressHolder, self).__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
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
    def __init__(self, name='' , email='',**kwargs):
        super(Contact, self).__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
class Supplier(Contact):
    def order(self,order):
        print("If This were a real system we will send"
        "'{}' order to '{}'".format(order,self.name))
class Friend(Contact,AddressHolder):
    def __init__(self,phone='',**kwargs):
        super(Friend, self).__init__(**kwargs)
        """
         **kwargs parameter 
        to capture any additional parameters that our particular method doesn't know what
        to do with. It passes these parameters up to the next class with the super call.

        """
        # Contact.__init__(self,name,email)
        # AddressHolder.__init__(self,street,state,city,code)
        # super(Friend,self).__init__(name,email)
        self.phone = phone

class MailSender:
    def send_mail(self, message):
        print ("Sending Email to "+ self.email)
        #add email logic here

class EmailableContact(Contact,MailSender):
    pass

