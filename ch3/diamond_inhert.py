class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print ("Calling method in base Class")
        self.num_base_calls += 1

