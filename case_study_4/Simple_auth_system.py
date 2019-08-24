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

class AuthException(Exception):
    def __init__(self,username,user=None):
        super(AuthException, self).__init__(username ,user)
        self.username = username
        self.user = user
class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass
class Authenticator:
    def __init__(self):
        '''Construct an authenticator to manage
        users logging in and out.'''
        self.users = {}

    def add_user(self,username , password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6 :
            raise PasswordTooShort(username)
        self.users[username] = User(username , password)
