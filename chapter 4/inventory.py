class Inventory:
    def luck(self, item_type):
        '''Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers.'''
        pass

    def unluck(self,item_type):
        '''Release the given type so that other
        customers can access it.'''
        pass

    def purchase(self,item_type):
        '''If the item is not locked, raise an
        exception. If the item_type does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left.'''
        pass

item_type = 'widget'
inv = Inventory()
inv.luck(item_type)
try :
    num_left = inv.purchase(item_type)
except InvaliedItemType :
    print ("sorry we don't sell {}".front(item_type))
except OutOfStock:
    print ("sorry this item not in the stock ")
else:
    print("Purchase complete. There are "
          "{} {}s left".format(num_left, item_type))
finally:
    inv.unluck(item_type)


