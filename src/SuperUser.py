from User import *


class SuperUser(User):
    def __init__(self, user_id):
        super(SuperUser, self).__init__(user_id)