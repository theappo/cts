from GateWay import *

class User():
	def __init__(self,user_id,user_password,balance,user_type,email,address):
		self.user_id = user_id
		self.user_password = user_password
		self.balance = user_balance
		self.user_type = user_type
		self.email = email
		self.address = address
	
	
	# def get_balance(self):
	# 	db = GateWay()
	# 	return db.get_balance(self.user_id)

	# def update_balance(self,offset):
	# 	db = GateWay()
	# 	return db.update_balance(self.user_id,offset)

	# def update_password(self,new_password):
	# 	db = GateWay()
	# 	return db.update_password(self.user_id,new_password)

	# def get_email(self):
	# 	db=GateWay()
	# 	return db.get_email(self.user_id)

	# def update_email(self,new_email):
	# 	db = GateWay()
	# 	return db.update_email(self.user_id,new_email)

	# def get_address(self):
	# 	db=GateWay()
	# 	return db.get_address(self.user_id)


	# def update_address(self.user_id,new_address):
	# 	db = GateWay()
	# 	return db.update_address(self.user_id,new_address)


# print(User(1).get_user_id())
	
