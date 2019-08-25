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
            except auth.InvalidUsername:
                print ("Sorry user name does not exist ")
            except auth.InvalidPassword:
                print ("sorry password is wrong")

            else:
                self.username = username

    def is_permitted(self,permission):
        try:
            auth.authorizor.check_permission(permission ,self.username)
        except auth.NotLoggedInError as e :
            print ("{} is not logged in ".format(self.username) )
            return False
        except auth.NotPermittedError as e :
            print ("{} can not {} ".format(self.username , permission))
            return  False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print ("testing program now")
    def change(self):
        if self.is_permitted("change program"):
            print ("Changing program now")

    def quite(self):
        raise SystemExit()

    def menu(self):
        answer = " "
        while True:
            print("""
            Please enter a command:
            \tlogin\tLogin
            \ttest\tTest the program
            \tchange\tChange the program
            \tquit\tquite
            """)
            answer = input("Enter command ").lower()
            try:
                func = self.menu_map[answer]
            except KeyError :
                print ("{} is not valied option ".format(answer))
            else:
                func()
            finally:
                print("thank you for testing the auth module")

Editor().menu()