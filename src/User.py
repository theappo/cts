from GateWay import *

class User():
	def __init__(self,user_id):
		self._user_id = user_id

	
	def get_user_id(self):
		return self._user_id

	# def get_blance():
	# 	db = GateWay()
	# 	return db.get_blance(self.id)


# print(User(1).get_user_id())
	