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

main()