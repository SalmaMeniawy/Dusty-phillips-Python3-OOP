class property:
    def __init__(self,baths='',beds='',square_feet='',**kwargs):
        super(property,self).__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths
    

