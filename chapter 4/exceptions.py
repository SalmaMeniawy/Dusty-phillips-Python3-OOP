"""
    we can! Here's a simple class that adds items
    to a list only if they are even numbered integers:

"""
class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError("only integer can be added ")
        if integer % 2 :
            raise ValueError("Only Even numbers can be added ")
        super(EvenOnly, self).append(integer)

