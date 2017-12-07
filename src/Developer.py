from User import *


class Developer(User):
    def __init__(self, user_id):
        super(Developer, self).__init__(user_id)
        self.db = GateWay()

    def current_indiv_projects(self):
        return self.db.get_devs_current_projects(self.user_id)

    def finished_indiv_projects(self):
        return self.db.get_devs_finished_projects(self.user_id)

#print(Developer("testuser10").finished_indiv_projects())
