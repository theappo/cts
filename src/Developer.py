from User import *


class Developer(User):
    def __init__(self, user_id):
        super(Developer, self).__init__(user_id)

# print(Developer(1).get_user_id())
