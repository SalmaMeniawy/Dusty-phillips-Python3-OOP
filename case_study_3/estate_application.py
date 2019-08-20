class property:
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

    def prompt_init(self):
        return dict(
            square_feet=input("Enter the square feet"),
            beds=input("Enter Number of Bedrooms"),
            baths=input("Enter Number of baths"),
        )

    prompt_init = staticmethod(prompt_init)
