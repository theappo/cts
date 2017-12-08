import sys

sys.path.insert(0, "../gui")

from User import *
from Team import *
from GateWay import *

class ApplicationManager():
    def __init__(self):
        self.apps = []
        self.db = GateWay()

    def read(self):
        self.apps = []

        list = self.db.get_applications()

        for app in list:
            self.apps.append(User(app[0]))

    def accept(self, i):
        self.db.approve_user_id(self.apps[i].user_id)

    def reject(self, i, reason):
        self.db.add_blacklist(self.apps[i].user_id, reason)
