import hashlib
class User :
    def __init__(self,username ,password):
        self.username = username
        self.password = self.encrypt_pw(password)
        self.is_log_in = False

        
