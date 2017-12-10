import sys

sys.path.insert(0, "../gui")

from User import *
from Team import *
from Developer import *
from GateWay import *

class TeamManager():
    def __init__(self):
        self.dev = []
        self.teams = []
        self.db = GateWay()
    
    def read(self, dev):
        self.dev = []
        self.teams = []
        
        self.dev = dev

        for team in dev.get_team():
            self.teams.append(Team(team[0]))

    def project(self, i):
        return self.teams[i].get_current_projects()

#t = TeamManager()
#t.read(Developer("testuser4"))
#print(t.project(0))