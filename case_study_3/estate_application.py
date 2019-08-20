class Property:
    def __init__(self, baths='', beds='', square_feet='', **kwargs):
        super(property, self).__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        'display method that display and print the propert attributes '
        print ("Property details ")
        print ("====================")
        print ("Square Foots : {}").format(self.square_feet)
        print ("bedrooms : {}").format(self.num_bedrooms)
        print ("bathrooms : {}").format(self.num_baths)
        print ()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)

class Apartment(Property):
    valied_laundries = ("coin","ensuite","none")
    valied_balaconies = ("yes","no","solarium")

    def __init__(self,balcony='',laundry='',**kwargs):
        super(Apartment, self).__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry
        