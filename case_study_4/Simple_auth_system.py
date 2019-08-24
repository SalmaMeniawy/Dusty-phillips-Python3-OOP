import hashlib
class User :
    def __init__(self,username ,password):
        self.username = username
        self.password = self.encrypt_pw(password)
        self.is_log_in = False

    def encrypt_pw(self,password):
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdiget()

    def check_password(self,password):
        '''Return True if the password is valid for this
        user, false otherwise.'''
        encrypted = self.encrypt_pw(password)
        return encrypted == self.password
