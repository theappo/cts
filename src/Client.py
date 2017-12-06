from User import *


class Client(User):
    def __init__(self, user_id):
        super(Client, self).__init__(user_id)
        
    def pending_projects(self):
        db = GateWay()
        return db.get_clients_pending_projects(self.user_id)
    
    
print(Client("testuser2").pending_projects())
