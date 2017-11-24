from User import *

class Client(User):
	def __init__(self, user_id):
		super(Client,self).__init__(user_id)

# print(Client(1).get_user_id())
		

	