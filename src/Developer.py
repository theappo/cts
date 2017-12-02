from User import *


class Developer(User):
    def __init__(self, user_id):
        super(Developer, self).__init__(user_id)

    def get_current_projects(self):
        db = GataWay()
        return db.get_developer.current_project(self.id)
# print(Developer(1).get_user_id())