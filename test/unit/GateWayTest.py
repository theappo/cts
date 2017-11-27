import sys
sys.path.insert(0, "../../src")

from GateWay import *
from testAndPrint import *

def main():

	Manager = GateWay()

	# check_blacklist
	testAndPrint(Manager.check_blacklist("testuser2"),False)

	# verify_user
	testAndPrint(Manager.verify_user('if','2'), False)
	testAndPrint(Manager.verify_user('testuser2','test'),False)
	testAndPrint(Manager.verify_user('testuser2','password2'),True)

	# add testuser4 to blacklist, then remove
	testAndPrint(Manager.add_blacklist('testuser4'), True)
	testAndPrint(Manager.clear_blacklist(), True)


	# update test user balance and check if update successful
	testAndPrint(Manager.update_user_balance('testuser3', 2000.00), True)
	testAndPrint(Manager.get_user_balance('testuser3'), 2000.00)

	# test get_user_address, and update user_address
	testAndPrint(Manager.get_user_address('testuser2'), '123 40th St. Queens, NY')
	testAndPrint(Manager.set_user_address('testuser4', '456 70th Street, Queens, NY'), True)

	# test set_user_password
	testAndPrint(Manager.set_user_password('testuser4', 'password'), True)
	#test set and get_user_email
	testAndPrint(Manager.set_user_email('testuser4', 'testuser4@gmail.com'), True)
	testAndPrint(Manager.get_user_email('testuser4'), 'testuser4@gmail.com')

	# test add_user and approve user id
	testAndPrint(Manager.add_user('testuser5', '', 10000, 1, 'testuser5@gmail.com', '100 Convent Ave. NY, NY'), True)
	testAndPrint(Manager.approve_user_id('testuser5'), True)

	# test total number of devs and clients
	testAndPrint(Manager.get_dev_num(), 0)
	testAndPrint(Manager.get_client_num(), 3)

	# test most active client
	testAndPrint(Manager.get_active_client(), "testuser2")






main()