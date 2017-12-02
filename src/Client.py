from User import *


class Client(User):
    def __init__(self, user_id):
        super(Client, self).__init__(user_id)

    def get_current_projects(self):
        db = GataWay()
        return db.get_client_current_project(self.id)
# print(Client(1).get_user_id())
