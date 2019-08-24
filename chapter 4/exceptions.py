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
# for val in (0,"hello",50.0,13):
    # print ("Testing {}".format(val) ,end=" ")
    # print(funny_devision2(val))
def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError(" 13 is un lickely Number  ")
        return 100 / anumber
    except ZeroDivisionError :
        return "Enter a number rather than zero"
    except TypeError :
        return "Enter a numerical value"
    except ValueError:
        print ("no no not 13")
        raise
    """
        write native code to get the arguments that the class of exception take to its contractor we get it 
    """
# try:
#     raise ValueError("This is an argument")
# except ValueError as e:
#     print("Execption Arguments are ", e.args)
    # print("The exception arguments were".format(e.args) )
"""
    we write this code to descover two keywords 'finaly'and 'else' to make code execute if the exception occure or not
"""
import random
some_exceptions = [ValueError , TypeError ,IndexError ,None]
try:
    choice = random.choice(some_exceptions)
    print ("raising choice {}".format(choice))
    if choice :
        raise choice("An Error")
except ValueError :
    print ("Change a value error")
except TypeError :
    print ("caught a type error")
except Exception as e :
    print ("cought some other errors : %s" %(e.__class__.__name__))
else :
    print ("this code will appear when there is no exceptions")

finally:
    print ("this cleanup code is always called")


# funny_division3(13)
class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError("only integer can be added ")
        if integer % 2 :
            raise ValueError("Only Even numbers can be added ")
        super(EvenOnly, self).append(integer)

"""
    Here's a simple exception we might use in a banking application:
"""
class InvalidWithdrawal(Exception):
    def __init__(self,balance,amount):
        super(InvalidWithdrawal, self).__init__("account doesnot have ${}".format(amount))
        self.balance = balance
        self.amount = amount

    def overage(self):
        return self.amount - self.balance

# raise InvalidWithdrawal(25 , 50)
# raise InvalidWithdrawal("you don't have 50 $ in your account")
"""
    try to handel exception of Invalidwithdrawl class
"""
# try:
#     raise InvalidWithdrawal(25,50)
# except InvalidWithdrawal as e :
#     print ("I am sorry , but your withdrawl is"
#            "more than your baance by"
#            "${}".format(e.overage()))
#
"""
    create function create with exception
"""
def divided_with_exception(number , divisor):
    try:
        print ("{} / {} = {} ".format(
            number , divisor , number / divisor * 1.0
        ))
    except ZeroDivisionError:
        print ("you can't divide by zero ")

