class Application():
	
	def __init__(self,user_id,user_password,balance,user_type,email,address,deposit_amount):
		self.user_id = user_id
		self.user_password=user_password
		self.balance=balance
		self.user_type = user_type
		self.email = email
		self.address = address
		self.deposit_amount = deposit_amount
		
	
		
# a=Application(1,1,1)
# print(a.get_user_id(),a.get_user_type(),a.get_deposit_amount())