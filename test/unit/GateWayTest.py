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
	testAndPrint(Manager.add_blacklist('testuser4', 'testing'), True)
	testAndPrint(Manager.clear_blacklist(), True)

	# check if testuser2 is client
	testAndPrint(Manager.get_user_type('testuser2'), 1)

	# update test user balance and check if update successful
	testAndPrint(Manager.update_user_balance('testuser3', 2000.00), True)
	testAndPrint(Manager.get_user_balance('testuser3'), 'user balance')

	# test get_user_address, and update user_address
	testAndPrint(Manager.get_user_address('testuser2'), '123 40th St. Queens, NY')
	testAndPrint(Manager.set_user_address('testuser4', '456 70th Street, Queens, NY'), True)

	# test set_user_password
	testAndPrint(Manager.set_user_password('testuser4', 'password'), True)
	#test set and get_user_email
	testAndPrint(Manager.set_user_email('testuser4', 'testuser4@gmail.com'), True)
	testAndPrint(Manager.get_user_email('testuser4'), 'testuser4@gmail.com')

	# test add_user and approve user id, then remove user so test will pass next time
	testAndPrint(Manager.add_user('testremove', '', 10000, 1, 'testuser5@gmail.com', '100 Convent Ave. NY, NY'), True)
	testAndPrint(Manager.approve_user_id('testremove'), True)
	testAndPrint(Manager.delete_account('testremove'), True)

	# test total number of devs and clients
	testAndPrint(Manager.get_dev_num(), 5)
	testAndPrint(Manager.get_client_num(), 6)

	# test most active client and dev with most income, may fail when i edit tables more
	testAndPrint(Manager.get_active_clients(3), '3 clients')
	testAndPrint(Manager.get_active_devs(3), '3 devs')

	# test adding a new project, insert team bids, individual bids, and then choose one bid, then finish the project and delete record.
	testAndPrint(Manager.delete_project('testproject'), True)
	testAndPrint(Manager.create_new_project('testproject', 'testuser2', 'testproject', '2017-12-30', 1000, '2017-12-01'), True)
	testAndPrint(Manager.place_team_bid('testproject', 'testteam1', 500), True)
	testAndPrint(Manager.place_team_bid('testproject', 'testteam2', 250), True)
	testAndPrint(Manager.place_team_bid('testproject', 'testteam3', 600), True)
	testAndPrint(Manager.place_individual_bid('testproject', 'testuser4', 700), True)
	testAndPrint(Manager.place_individual_bid('testproject', 'testuser6', 600), True)
	testAndPrint(Manager.get_pending_projects(), '\n\nPendingProjects\n')
	testAndPrint(Manager.get_lowest_bid('testproject'), 'Lowest bid = 250')
	testAndPrint(Manager.get_individual_project_bids('testproject'), (('testuser6', 600.00), ('testuser4', 700.00)))
	testAndPrint(Manager.get_team_project_bids('testproject'), (('testteam2', 250.00), ('testteam1', 500.00), ('testteam3', 600.00)))
	testAndPrint(Manager.choose_team('testproject', 'testteam1', 500.00), True)
	testAndPrint(Manager.get_project_status('testproject'), 'Current')
	testAndPrint(Manager.get_project_type('testproject'), 'Team')
	testAndPrint(Manager.finish_team_project('testproject'), True)
	testAndPrint(Manager.create_team_project_review('testproject', 5, 'Good Project'), True)
	testAndPrint(Manager.get_dev_pending_reviews('testuser4', 'testproject'), 'pending reviews')
	testAndPrint(Manager.create_project_review('testproject', 'testuser4', 'testuser6', 5, 'gz'), True)
	testAndPrint(Manager.create_project_review('testproject', 'testuser6', 'testuser4', 5, 'gz'), True)
	testAndPrint(Manager.get_projectreviews('testuser6'), 'user6\'s project reviews')

	testAndPrint(Manager.get_applications(), 'applications')

	# makes another test project
	print('Testing project 2...\n\n')
	testAndPrint(Manager.delete_project('testproject2'), True)
	testAndPrint(Manager.create_new_project('testproject2', 'testuser5', 'testproject2', '2017-12-29', 1000, '2017-12-10'), True)
	testAndPrint(Manager.place_team_bid('testproject2', 'testteam2', 600.00), True)
	testAndPrint(Manager.choose_team('testproject2', 'testteam2', 600.00), True)
	testAndPrint(Manager.finish_team_project('testproject2'), True)
	testAndPrint(Manager.create_team_project_review('testproject2', 1, 'Bad Review'), True)
	testAndPrint(Manager.get_bad_projects(), 'list of bad projects')
	testAndPrint(Manager.settle_project_dispute('testproject2', 3, 600.00), True)
	testAndPrint(Manager.get_dev_pending_reviews('testuser4', 'testproject2'), 'user\'s pending reviews')
	testAndPrint(Manager.create_project_review('testproject2', 'testuser4', 'testuser5', 4, 'good project'), True)
	testAndPrint(Manager.create_project_review('testproject2', 'testuser4', 'testuser6', 2, ''), True)

	print('Done testing project 2...\n\n')


	# test getting user interests, and then ordering users by their interests
	testAndPrint(Manager.get_user_interests('testuser6'), (0, 0, 0, 1, 1, 1))
	testAndPrint(Manager.get_similar_interests('testuser6'), 'all users ordered by interests shared')

	# test searching functions
	testAndPrint(Manager.search_by_user_id('testuser'), 'list of all users with similar name')
	testAndPrint(Manager.search_by_team_id('testteam'), 'list of all teams with similar name')
	testAndPrint(Manager.search_by_teamprojectid('5'), 'list of projects')
	testAndPrint(Manager.search_by_indivprojectid('6'), 'list of projects')

	testAndPrint(Manager.new_message('testuser4', 'testuser6', 'testmessage'), '')
	testAndPrint(Manager.get_teams_users('testteam1'), '')

	testAndPrint(Manager.get_users_teams('testuser6'), 'user\'s teams')
	testAndPrint(Manager.get_team_projecthistory('testteam1'), 'teams project history')
	testAndPrint(Manager.get_devs_finished_team_projects('testuser4'), 'user4\'s team project history')







main()