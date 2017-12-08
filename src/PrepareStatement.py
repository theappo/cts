# check is user_id exists
user_id_exists = "SELECT user_id FROM users WHERE user_id = %s"

# insert new user
insert_user = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, 0)"

# remove user from application table
approve_user = "DELETE FROM application WHERE user_id = %s"

# remove user from system (foreign keys will cascade)
remove_user = "DELETE FROM users WHERE user_id = %s"

# insert new user into applications too
insert_applications = "INSERT INTO application (user_id) VALUES (%s)"

# get applications for superuser
get_applications = "SELECT * FROM application"

user_approved = "SELECT * FROM application WHERE user_id = %s"

# get user's type (0 = superuser, 1 = client, 2 = developer)
get_type = "SELECT user_type FROM users WHERE user_id = %s"

# search user_id in blacklist table
search_blacklist = "SELECT * FROM Blacklist WHERE user_id = %s"

# get number of warnings 0, 1, or 2
get_warnings = "SELECT warnings FROM users WHERE user_id = %s"
remove_warning = "UPDATE users SET warnings = 0 WHERE user_id = %s"

# add user_id to blacklist
add_to_blacklist = "INSERT INTO Blacklist VALUES (%s, UTC_DATE(), %s)"

# remove user from blacklist
remove_from_blacklist = "DELETE FROM Blacklist WHERE user_id = %s"

# search user_id and user_password in user table
verify_user = "SELECT user_type FROM users WHERE user_id = %s AND password = %s"

# test if username is taken
user_exists = "SELECT user_id FROM users WHERE user_id = %s"

# return user balance
user_balance = "SELECT balance FROM users WHERE user_id = %s"

# set user balance
update_balance = "UPDATE users SET balance = %s WHERE user_id = %s"

# return user address
get_address = "SELECT address FROM users WHERE user_id = %s"

# set user address
update_address = "UPDATE users SET address = %s WHERE user_id = %s"

# set user password
update_password = "UPDATE users SET password = %s WHERE user_id = %s"

# get user email
get_email = "SELECT email FROM users WHERE user_id = %s"

# set user email
update_email = "UPDATE users SET email = %s WHERE user_id = %s"

# count number of devs
count_devs = "SELECT count(*) FROM Developers"

# count number of clients
count_clients = "SELECT count(*) FROM Clients"

# get client with most projects
active_client = "SELECT client_id FROM Projects GROUP BY client_id ORDER BY count(*) DESC LIMIT %s"

# gets the dev with most income in transaction history (iterating through projects would take longer / more work)
active_dev = "SELECT receiver FROM transactionhistory WHERE receiver IN (SELECT user_id FROM users WHERE user_type = 2) GROUP BY receiver ORDER BY SUM(amount) DESC LIMIT %s"

# Create a project (must insert to projects and pendingprojects)
new_project = "INSERT Projects VALUES (%s, %s, %s, %s, NULL, %s, NOW())"
add_pending_project = "INSERT PendingProjects VALUES (%s, %s, %s)"
get_pending_projects = "SELECT p.project_id, p.client_id, p.description, p.date_posted, pp.bid_deadline, p.deadline FROM Projects p INNER JOIN PendingProjects pp ON p.project_id = pp.project_id"

get_project_info = "SELECT * FROM Projects WHERE project_id = %s"

# get user transaction history
get_transaction_history = "SELECT * FROM TransactionHistory WHERE sender = %s OR receiver = %s"
# enter transaction history
add_transaction = "INSERT TransactionHistory (amount, transaction_date, receiver, sender) VALUES (%s, NOW(), %s, %s)"

# remove project for testing purposes
remove_project = "DELETE FROM Projects WHERE project_id = %s"

# get project status
project_status = "SELECT project_status FROM Projects WHERE project_id = %s"

# get project type
project_type = "SELECT project_type FROM Projects WHERE project_id = %s"

# check if project name taken
project_exists = "SELECT project_id FROM Projects WHERE project_id = %s"

# team management
team_exists = "SELECT * FROM Teams WHERE team_id = %s"
create_team = "INSERT Teams VALUES (%s, %s, NULL, NULL, NULL, NULL)"
get_team_devs = "SELECT dev1, dev2, dev3, dev4, dev5 FROM Teams WHERE team_id = %s"
set_team_devs = "UPDATE Teams set %s = %s, %s = NULL WHERE team_id = %s"
set_team_devs11 = "UPDATE Teams set dev1 = %s, dev1 = NULL WHERE team_id = %s"
set_team_devs12 = "UPDATE Teams set dev1 = %s, dev2 = NULL WHERE team_id = %s"
set_team_devs13 = "UPDATE Teams set dev1 = %s, dev3 = NULL WHERE team_id = %s"
set_team_devs14 = "UPDATE Teams set dev1 = %s, dev4 = NULL WHERE team_id = %s"
set_team_devs15 = "UPDATE Teams set dev1 = %s, dev5 = NULL WHERE team_id = %s"
set_team_devs22 = "UPDATE Teams set dev2 = %s, dev2 = NULL WHERE team_id = %s"
set_team_devs33 = "UPDATE Teams set dev3 = %s, dev3 = NULL WHERE team_id = %s"
set_team_devs44 = "UPDATE Teams set dev4 = %s, dev4 = NULL WHERE team_id = %s"
set_team_devs55 = "UPDATE Teams set dev5 = %s, dev5 = NULL WHERE team_id = %s"
set_team_devs23 = "UPDATE Teams set dev2 = %s, dev3 = NULL WHERE team_id = %s"
set_team_devs24 = "UPDATE Teams set dev2 = %s, dev4 = NULL WHERE team_id = %s"
set_team_devs25 = "UPDATE Teams set dev2 = %s, dev5 = NULL WHERE team_id = %s"
set_team_devs34 = "UPDATE Teams set dev3 = %s, dev4 = NULL WHERE team_id = %s"
set_team_devs35 = "UPDATE Teams set dev3 = %s, dev5 = NULL WHERE team_id = %s"
set_team_devs45 = "UPDATE Teams set dev4 = %s, dev5 = NULL WHERE team_id = %s"





add_to_team1 = "UPDATE Teams set dev1 = %s WHERE team_id = %s"
add_to_team2 = "UPDATE Teams set dev2 = %s WHERE team_id = %s"
add_to_team3 = "UPDATE Teams set dev3 = %s WHERE team_id = %s"
add_to_team4 = "UPDATE Teams set dev4 = %s WHERE team_id = %s"
add_to_team5 = "UPDATE Teams set dev5 = %s WHERE team_id = %s"


# place the team or individual bids
place_teambid = "INSERT Team_Bid_Project VALUES (%s, %s, %s)"
place_indivbid = "INSERT Individual_Bid_Project VALUES (%s, %s, %s)"

# get the project bids
individual_bids = "SELECT user_id, bid FROM Individual_Bid_Project WHERE project_id = %s ORDER BY bid ASC"
team_bids = "SELECT team_id, bid FROM Team_Bid_Project WHERE project_id = %s ORDER BY bid ASC"

# puts bid into currecurrent project table, also clears bid table of the project, same for individual chosen
choose_team_bid = "INSERT INTO Current_Team_Project VALUES (%s, %s, %s)"
choose_indiv_bid = "INSERT INTO Current_Individual_Project VALUES (%s, %s, %s)"
transferfunds1 = "INSERT INTO TransactionPending (amount, transaction_date, receiver, sender, project_id) VALUES (%s, NOW(), %s, (SELECT client_id FROM Projects WHERE project_id = %s), %s)"
transferfunds2 = "INSERT INTO TransactionHistory (amount, transaction_date, receiver, sender) (SELECT amount, NOW(), receiver, sender FROM TransactionPending WHERE project_id = %s)"
canceltransfer = "DELETE FROM TransactionPending WHERE project_id = %s"

# gets all from current project record
get_current_team_project_info = "SELECT * FROM Current_Team_Project WHERE project_id = %s"
get_current_indiv_project_info = "SELECT * FROM Current_Individual_Project WHERE project_id = %s"

# gets all from finished project record
get_finished_indiv_project = "SELECT * FROM Finished_Individual_Project WHERE project_id = %s"
get_finished_team_project = "SELECT * FROM Finished_Team_Project WHERE project_id = %s"

# puts current project into finished table
team_finished = "INSERT INTO Finished_Team_Project VALUES (%s, NULL, %s, NULL, %s, NOW())"
indiv_finished = "INSERT INTO Finished_Individual_Project VALUES (%s, %s, %s, NOW())"

# enters a review
make_project_review = "INSERT INTO ProjectReviews VALUES (%s, %s, %s, %s, %s)"
# enters a teamproject review (from client)
make_team_project_review = "UPDATE Finished_Team_Project SET teamrating = %s, teamreview = %s WHERE project_id = %s"
# enter a review between team mates
make_team_review = "INSERT TeamReviews VALUES (%s, %s, %s, %s, %s)"
update_team_review = "UPDATE ProjectReviews SET rating = %s WHERE project_id = %s"
update_team_project_review = "UPDATE Finished_Team_Project SET teamrating = %s, bid = %s WHERE project_id = %s"
update_indiv_project_review = "UPDATE Finished_Individual_Project SET bid = %s WHERE project_id = %s"
get_bad_projects = "SELECT tp.project_id, pr.rating, SUM(tp.amount) FROM TransactionPending tp INNER JOIN ProjectReviews pr ON tp.project_id = pr.project_id  AND tp.receiver = pr.receiver_id WHERE pr.rating <= 2 GROUP BY tp.project_id"
get_dev_pending_client_reviews = "SELECT p.project_id, p.client_id FROM Projects p INNER JOIN Finished_Individual_Project fip ON p.project_id = fip.project_id WHERE fip.dev_id = %s AND fip.dev_id NOT IN (SELECT receiver_id FROM ProjectReviews WHERE project_id = p.project_id AND sender_id = p.client_id)"
get_review = "SELECT * FROM ProjectReviews WHERE sender_id = %s AND receiver_id = %s AND project_id = %s"

# get all the clients overdue projects
get_client_overdue_projects2 = "SELECT project_id FROM Projects WHERE client_id = %s AND deadline < NOW()"
# gets all pending projects where deadline has passed
get_client_overdue_projects = "SELECT p.project_id FROM PendingProjects pp INNER JOIN Projects p WHERE p.client_id = %s AND pp.bid_deadline > NOW()"

# get all the current project for developer
get_developer_current_projects = "SELECT project_id FROM Current_Individual_Project WHERE developer_id = %s"

# get all the current project for a teamreview
get_team_current_projects = "SELECT project_id FROM Current_Team_Project WHERE team_id = %s"

# get all inbox message
inbox_message = "SELECT sender, message, time FROM Messages where receiver = %s"

# get sent message
sent_message = "SELECT receiver, message, time FROM Messages where sender = %s"

# new message
new_message = "INSERT INTO Messages (sender, receiver, message, time) VALUES (%s, %s, %s, NOW())"

# update interests, get the users interests, also find similar interests
update_interests = "UPDATE UserInterests SET Java = %s, Python = %s, Cpp = %s, IOS = %s, Android = %s, DesktopApp = %s WHERE user_id = %s"
get_user_interests = "SELECT Java, Python, Cpp, IOS, Android, DesktopApp FROM UserInterests WHERE user_id = %s"
find_similar_interests = "SELECT user_id FROM UserInterests WHERE user_id not in (%s) GROUP BY user_id ORDER BY abs (Java - %s) + abs (Python - %s) + abs (Cpp - %s) + abs (IOS - %s) + abs (Android - %s) + abs (DesktopApp - %s) ASC"

# Search Statements
# find all users/projects with substring in their id
search_users = "SELECT user_id, user_type FROM Users WHERE user_id LIKE %s"
search_teams = "SELECT team_id FROM Teams WHERE team_id LIKE %s"
search_team_finished_projects = "SELECT ftp.project_id, client_id, description, team_id, bid FROM Finished_Team_Project ftp INNER JOIN Projects p ON ftp.project_id = p.project_id WHERE ftp.project_id LIKE %s"
search_indiv_finished_projects = "SELECT fip.project_id, client_id, description, dev_id, bid FROM Finished_Individual_Project fip INNER JOIN Projects p ON fip.project_id = p.project_id WHERE fip.project_id LIKE %s"
get_project_teamdevs = "SELECT dev1, dev2, dev3, dev4, dev5 FROM TeamHistory WHERE team_id = %s AND time_formed < %s ORDER BY time_formed DESC LIMIT 1"
get_project_teamdevs2 = "SELECT dev1, dev2, dev3, dev4, dev5 FROM TeamHistory WHERE team_id = %s AND time_formed < NOW() ORDER BY time_formed DESC LIMIT 1"
get_project_team = "SELECT th.dev1, th.dev2, th.dev3, th.dev4, th.dev5 FROM TeamHistory th INNER JOIN Finished_Team_Project ftp ON th.team_id = ftp.team_id where ftp.project_id = %s AND th.time_formed < ftp.date_submit ORDER BY th.time_formed DESC LIMIT 1"
get_user_reviews = "SELECT * FROM ProjectReviews WHERE receiver_id = %s"
get_teamhistory = "SELECT * FROM Finished_Team_Project WHERE team_id = %s"
get_users_teams = "SELECT team_id FROM teams WHERE dev1 = %s OR dev2 = %s OR dev3 = %s OR dev4 = %s OR dev5 = %s"
get_teams_users = "SELECT dev1, dev2, dev3, dev4, dev5 FROM teams WHERE team_id = %s"

# get user's projects:
get_client_pending_projects = "SELECT * FROM Projects p INNER JOIN PendingProjects pp ON p.project_id = pp.project_id WHERE p.client_id = %s"
get_client_current_indiv_projects = "SELECT * FROM Projects p INNER JOIN Current_Individual_Project cip ON p.project_id = cip.project_id WHERE p.client_id = %s"
get_client_current_team_projects = "SELECT * FROM Projects p INNER JOIN Current_Team_Project ctp ON p.project_id = ctp.project_id WHERE p.client_id = %s"
get_clients_finished_indiv_projects = "SELECT * FROM Projects p INNER JOIN Finished_Individual_Project fip ON p.project_id = fip.project_id WHERE p.client_id = %s"
get_clients_finished_team_projects = "SELECT * FROM Projects p INNER JOIN Finished_Team_Project ftp ON p.project_id = ftp.project_id WHERE p.client_id = %s"
get_dev_bids = "SELECT * FROM Projects p INNER JOIN Individual_Bid_Project ibp ON p.project_id = ibp.project_id WHERE ibp.user_id = %s"
get_dev_current_projects = "SELECT * FROM Projects p INNER JOIN Current_Individual_Project cip ON p.project_id = cip.project_id WHERE cip.developer_id = %s"
get_dev_finished_projects = "SELECT * FROM Projects p INNER JOIN Finished_Individual_Project fip ON p.project_id = fip.project_id WHERE fip.dev_id = %s"
get_dev_finished_team_projects = "SELECT p.*, ftp.* FROM (Projects p INNER JOIN Finished_Team_Project ftp ON p.project_id = ftp.project_id) INNER JOIN TeamHistory th ON th.team_id = ftp.team_id WHERE %s IN (th.dev1, th.dev2, th.dev3, th.dev4, th.dev5) AND th.time_formed < ftp.date_submit ORDER BY th.time_formed DESC LIMIT 1"
get_team_bids = "SELECT * FROM Projects p INNER JOIN Team_Bid_Project tbp ON p.project_id = tbp.project_id WHERE tbp.team_id = %s"
get_team_current_projects = "SELECT * FROM Projects p INNER JOIN Current_Team_Project ctp ON p.project_id = ctp.project_id WHERE ctp.team_id = %s"
get_team_finished_projects = "SELECT * FROM Projects p INNER JOIN Finished_Team_Project ftp ON p.project_id = ftp.project_id WHERE ftp.project_id = %s"






