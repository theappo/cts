class Application():
	
	def __init__(self, user_id,user_type,deposit_amount):
		self._user_type = user_type
		self._user_id = user_id
		self._deposit_amount=deposit_amount

	def get_user_id(self):
		return self._user_id

	def get_user_type(self):
		return self._user_type

	def get_deposit_amount(self):
		return self._deposit_amount
		
# a=Application(1,1,1)
# print(a.get_user_id(),a.get_user_type(),a.get_deposit_amount())