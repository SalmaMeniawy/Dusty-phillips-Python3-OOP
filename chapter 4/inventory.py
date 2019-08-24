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
