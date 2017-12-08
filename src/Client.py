from User import *


class Client(User):
    def __init__(self, user_id):
        super(Client, self).__init__(user_id)

    def pending_projects(self):
        return self.db.get_clients_pending_projects(self.user_id)

    def current_indiv_projects(self):
        return self.db.get_clients_current_indiv_projects(self.user_id)

    def current_team_projects(self):
        return self.db.get_clients_current_team_projects(self.user_id)

    def finished_indiv_projects(self):
        return self.db.get_clients_finished_indiv_projects(self.user_id)

    def finished_team_projects(self):
        return self.db.get_clients_finished_team_projects(self.user_id)

