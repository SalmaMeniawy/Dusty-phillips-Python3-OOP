"""
    we can! Here's a simple class that adds items
    to a list only if they are even numbered integers:

"""
def no_return():
    print ("I am about to rain exception ")
    raise Exception("this is always raised")
    print ("this line will not execute")
    return  "I won't be returned"

def raise_exceptor():
    print ("call_exceptor call here")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")

# try:
#     no_return()
# except:
#     print("I cought an exception")
print ("Excecution after the exception")

def funny_division(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        # return "Zero is not a good idea"
        return raise_exceptor()

# print (funny_division(0))
# print (funny_division("sss"))
def funny_devision2(anumber):
    try:
        if anumber == 13:
            raise ValueErrpr("13 is not a lucky number")
        return 100 / anumber
    except (TypeError , ZeroDivisionError):
        return "Enter number rather than Zero"
for val in (0,"hello",50.0,13):
    print ("Testing {}".format(val) ,end=" ")
    print(funny_devision2(val))

class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError("only integer can be added ")
        if integer % 2 :
            raise ValueError("Only Even numbers can be added ")
        super(EvenOnly, self).append(integer)

