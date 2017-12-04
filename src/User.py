from GateWay import *


class User():
    def __init__(self, user_id):
        self.user_id = user_id

    def update_password(self, new_password):
        db = GateWay()
        return db.set_user_password(self.user_id, new_password)

    def get_balance(self):
        db = GateWay()
        return db.get_user_balance(self.user_id)

    def update_balance(self, new_balance):
        db = GateWay()
        return db.update_user_balance(self.user_id, new_balance)

    def get_email(self):
        db = GateWay()
        return db.get_user_email(self.user_id)

    def update_email(self, new_email):
        db = GateWay()
        return db.set_user_email(self.user_id, new_email)

    def get_address(self):
        db = GateWay()
        return db.get_user_address(self.user_id)

    def update_address(self, new_address):
        db = GateWay()
        return db.update_address(self.user_id, new_address)

    # return () if no transaction history
    def get_transaction_history(self):
        db = GateWay()
        return db.get_transaction_history(self.user_id, self.user_id)

    def get_inbox_message(self):
        db = GateWay()
        return db.get_inbox_message(self.user_id)

    def get_sent_message(self):
        db = GateWay()
        return db.get_sent_message(self.user_id)

    def new_message(self, receiver, message):
        db = GateWay()
        return db.new_message(self.user_id, receiver, message)

    def interests(self):
        db = GateWay()
        return db.get_user_interests(self.user_id)

    def type(self):
        db = GateWay()
        user_type = db.get_user_type(self.user_id)
        if user_type == 0:
            return "Super User"
        elif user_type == 1:
            return "Client"
        else:
            return "Develop"

    #TODO: add aveger rating
    def rating(self):
        db = GateWay()
        return "4.6"

    #TODO: use in a team?
    #TODO: all reveiw
    #TODO: all history porject

u = User("okokokok")
print(u.get_sent_message())