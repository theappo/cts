from GateWay import *

class Project():
    def __init__(self, project_id, client_id, description, deadline):
        self.project_id = project_id
        self.client_id = client_id
        self.description = description
        self.deadline = deadline
        self.db = GateWay()
