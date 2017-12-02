from User import *
from SuperUser import *
from Client import *
from Developer import *
from GateWay import *

from PyQt5.QtWidgets import QMessageBox


class LoginManager():
    def __init__(self):
        self.currentUser = None

    def login(self, user_id, password):
        db = GateWay()

        if db.check_blacklist(user_id):
            self.currentUser = None
            return db.check_blacklist(user_id)[0][1]
        elif db.verify_user(user_id, password):
            user_type = db.get_user_type(user_id)

            if user_type == 0:
                self.currentUser = SuperUser(user_id)
            elif user_type == 1:
                self.currentUser = Client(user_id)
            else:
                self.currentUser = Developer(user_id)
        #TODO: add user to blacklist if wanring = 2
            return "Welcome"

        else:
            self.currentUser = None
            return "INVALID USER ID OR PASSWORD"

    def log_out(self):
        self.currentUser = None
