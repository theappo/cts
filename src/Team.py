from GateWay import *

class Team():
    def __init__(self, team_id):
        self.team_id = team_id
        self.db = GateWay()

    def add_member(self,user_id):
        return self.db.add_to_team(self.team_id, user_id)

    def get_team_members(self):
        return self.db.get_team_devs(self.team_id)

    def get_current_projects(self):
        return self.db.get_team_current_projects(self.team_id)

    def get_history_projects(self):
        return self.db.get_team_finished_projects(self.team_id)

#print((Team("testteam1").get_history_projects()))

