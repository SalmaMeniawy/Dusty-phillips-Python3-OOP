class Editor:

    import auth
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login ,
            "test":self.test ,
            "change":self.change ,
            "quite" : self.quite
        }

