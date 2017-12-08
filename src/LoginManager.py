from User import *
from SuperUser import *
from Client import *
from Developer import *
from GateWay import *


class LoginManager():
    def __init__(self):
        self.currentUser = None

    def login(self, user_id, password):
        db = GateWay()

        if db.check_blacklist(user_id):
            self.currentUser = None
            return db.get_black_list(user_id)[0]
        elif db.verify_user(user_id, password):
            user_type = db.get_user_type(user_id)

            if user_type == 0:
                self.currentUser = SuperUser(user_id)
            elif user_type == 1:
                self.currentUser = Client(user_id)
            else:
                self.currentUser = Developer(user_id)

            if db.check_warning_number(user_id) >= 2:
                db.add_blacklist(user_id, "Due to your low performance, you have been add to the blacklist")
                return "This is your last time login"

            return "Welcome"

        else:
            self.currentUser = None
            return "INVALID USER ID OR PASSWORD"

    def log_out(self):
        self.currentUser = None
