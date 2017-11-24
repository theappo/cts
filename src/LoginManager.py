from User import *
from GateWay import *

def login(user_id, password):
	db = GateWay();
	if db.check_blacklist(user_id):
		return None
	elif db.verify_user(user_id,password):
		return 1
		# if db.check_user_type(user_id)==2:
		# 	return Developer(user_id)
		# if db.check_user_type(user_id)==1:
		# 	return Client(user_id)
		# if db.check_user_type(user_id)==0:
		# 	return SuperUser(user_id)
	else:
		return None
login("testuser2","password2")
