from User import *


class Developer(User):
    def __init__(self, user_id):
        super(Developer, self).__init__(user_id)
        self.db = GateWay()

    def current_indiv_projects(self):
        return self.db.get_devs_current_projects(self.user_id)

    def finished_indiv_projects(self):
        return self.db.get_devs_finished_projects(self.user_id)

    def finished_team_projects(self):
        return self.db.get_devs_finished_team_projects(self.user_id)

    def get_dev_pending_client_reviews(self):
        return self.db.get_dev_pending_client_reviews(self.user_id)

    def get_team(self):
        return self.db.get_users_teams(self.user_id)

    def create_team(self, team_id):
        self.db.create_team(team_id, self.user_id)

    def join_team(self, team_id):
        self.db.add_to_team(team_id, self.user_id)

    def leave_team(self, team_id):
        self.db.remove_from_team(team_id, self.user_id)

#print(Developer("testuser4").get_team())