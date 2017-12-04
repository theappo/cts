import sys

sys.path.insert(0, "../gui")

from User import *
from Team import *
from GateWay import *

class SearchEngine():
    def __init__(self):
        self.users = []
        self.teams = []
        self.idprojs = []
        self.teamprojs = []

    def search(self, keyword):
        db = GateWay()

        # empty all result list
        self.users = []
        self.teams = []
        self.idprojs = []
        self.teamprojs = []

        userlist = db.search_by_user_id(keyword)

        for i in range(len(userlist)):
            self.users.append(User(userlist[i][0]))

        teamlist = db.search_by_team_id(keyword)

        for i in range(len(teamlist)):
            self.teams.append(Team(teamlist[i][0]))

        self.idprojs = db.search_by_indivprojectid(keyword)

        self.teamprojs = db.search_by_teamprojectid(keyword)