class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print ("Calling method in base Class")
        self.num_base_calls += 1


class LeftClass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print ("Print calling method in left class")
        self.num_left_calls += 1
