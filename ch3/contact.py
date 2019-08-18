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
