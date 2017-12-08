from GateWay import *


class User():
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = GateWay()

    def update_password(self, new_password):
        return self.db.set_user_password(self.user_id, new_password)

    def get_balance(self):
        return self.db.get_user_balance(self.user_id)

    def update_balance(self, new_balance):
        return self.db.update_user_balance(self.user_id, new_balance)

    def get_email(self):
        return self.db.get_user_email(self.user_id)

    def update_email(self, new_email):
        return self.db.set_user_email(self.user_id, new_email)

    def get_address(self):
        return self.db.get_user_address(self.user_id)

    def update_address(self, new_address):
        return self.db.update_address(self.user_id, new_address)

    # return () if no transaction history
    def get_transaction_history(self):
        return self.db.get_transaction_history(self.user_id, self.user_id)

    def get_inbox_message(self):
        return self.db.get_inbox_message(self.user_id)

    def get_sent_message(self):
        return self.db.get_sent_message(self.user_id)

    def new_message(self, receiver, message):
        return self.db.new_message(self.user_id, receiver, message)

    def interests(self):
        return self.db.get_user_interests(self.user_id)

    def type(self):
        user_type = self.db.get_user_type(self.user_id)
        if user_type == 0:
            return "Super User"
        elif user_type == 1:
            return "Client"
        else:
            return "Develop"

    def black_reason(self):
        return self.db.get_black_list(self.user_id)[0]

    def rating(self):
        try:
            return round(self.db.average_rating(self.user_id), 2)
        except TypeError:
            return None

    def get_review(self):
        return self.db.get_projectreviews(self.user_id)

    def check_application(self):
        return self.db.check_application(self.user_id)

#u = User("123456")
#print(u.get)