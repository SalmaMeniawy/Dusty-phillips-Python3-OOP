def get_valid_input(input_string, valied_options):
    input_string += "({})".format(" ,".join(valied_options))
    responce = input(input_string)
    while responce.lower() not in valied_options:
        responce = input(input_string)
    return responce

class Property:
    def __init__(self, baths='', beds='', square_feet='', **kwargs):
        super(Property, self).__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        'display method that display and print the propert attributes '
        print ("Property details ")
        print ("====================")
        print ("Square Foots : {} ".format(self.square_feet))
        print ("bedrooms : {} ".format(self.num_bedrooms))
        print ("bathrooms : {} ".format(self.num_baths))
        print ()
    @staticmethod
    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    # prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    valied_laundries = ("coin", "ensuite", "none")
    valied_balaconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super(Apartment, self).__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super(Apartment, self).display()
        print("Apartment Details")
        print ("laundary : %s" % self.laundry)
        print ("has balcony : %s" % self.balcony)


    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valied_laundries
        )
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valied_balaconies
        )
        # laundry = ''
        # while laundry.lower() not in \
        #         Apartment.valied_laundries:
        #     laundry = input("What laundry facilites does "
        #                     "the proparty have ? ({})".format(
        #         ", ".join(Apartment.valied_laundries)
        #     ))
        # balcony = ''
        # while balcony.lower() not in \
        #         Apartment.valied_balaconies:
        #     balcony = input(
        #         "Does Property have a balcony ? "
        #         "({})".format(
        #             ", ".join(Apartment.valied_balaconies)
        #
        #         )
        #     )
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    # prompt_init = staticmethod(prompt_init)

class House(Property):
    valied_garage = ("attached","detached","none")
    valied_fenced = ("yes","no")

    def __init__(self,num_stories='',garage='',fenced='',**kwargs):
        super(House, self).__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    # def display(self):def display(self):
    # super().display()
    # print("HOUSE DETAILS")
    # print("# of stories: {}".format(self.num_stories))
    # print("garage: {}".format(self.garage))
    # print("fenced yard: {}".format(self.fenced))

    def display(self):
        super(House,self).display()
        print("HOUSE DETAILS")
        print("# of stories: {} ".format(self.num_stories))
        print("garage: {} ".format(self.garage))
        print("fenced yard: {} ".format(self.fenced ))
    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("is the yard fenced",
                                 House.valied_fenced)
        garage = get_valid_input("is There a garage ? ",
                                 House.valied_garage)
        num_strories = input("How many stories ?")

        parent_init.update({
            "fenced":fenced ,
            "garage":garage ,
            "num_stories":num_strories
        })
        return parent_init
    # prompt_init = staticmethod(prompt_init)

class Purchase:
    def __init__(self,taxes='',price='',**kwargs):
        super(Purchase, self).__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super(Purchase, self).display()
        print ("Purchase Price : {} ".format(self.price))
        print ("Purchase Taxes : {} ".format(self.taxes))
    @staticmethod
    def prompt_init():
        return dict(
            price= input("what is the selling price ?"),
            taxes = input("what are the estimated taxes ? ")
        )
    # prompt_init = staticmethod(prompt_init)
class Rental:
    def __init__(self, furnished='', utilities='',
        rent='', **kwargs):
        super(Rental,self).__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities
    def display(self):
        super(Rental,self).display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))
    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    # prompt_init = staticmethod(prompt_init)
class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
# prompt_init = staticmethod(prompt_init)


class ApartmentRental(Apartment ,Rental):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase , Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return  init