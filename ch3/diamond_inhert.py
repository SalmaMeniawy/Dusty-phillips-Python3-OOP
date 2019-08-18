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

class RightClass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print ("print calling merthod in right class")
        self.num_right_calls += 1


class SubClass(LeftClass , RightClass):
    num_sub_calls = 0

    def call_me(self):
        LeftClass.call_me(self)
        RightClass.call_me(self)
        print ("print calling method in sub class")
        self.num_sub_calls += 1