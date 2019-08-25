import auth
class Editor:


    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login ,
            "test":self.test ,
            "change":self.change ,
            "quite" : self.quite
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username : ")
            password = input("password : ")
            try :
                auth.authenticator.login(username ,password)
            except auth.InvalidUsername(username):
                print ("Sorry user name does not exist ")
            except auth.InvalidPassword(username ,password ):
                print ("sorry password is wrong")

            else:
                self.username = username