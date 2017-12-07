from Project import *


class PendingProject(Project):
    def __init__(self, project_id, client_id, description, deadline):
        super(PendingProject, self).__init__(project_id, client_id, description, deadline)

    def individual_bids(self):
        return self.db.get_individual_project_bids(self.project_id)

print(PendingProject("0","testuser2","","2017-12-30" ).individual_bids())