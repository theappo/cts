# check is user_id exists
user_id_exists = "SELECT user_id FROM users WHERE user_id = %s"

# insert new user
insert_user = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"

# remove user from application table
approve_user = "DELETE FROM application WHERE user_id = %s"

# remove user from system (foreign keys will cascade)
remove_user = "DELETE FROM users WHERE user_id = %s"

# insert new user into applications too
insert_applications = "INSERT INTO application VALUES (%s)"

# get user's type (0 = superuser, 1 = client, 2 = developer)
get_type = "SELECT user_type FROM users WHERE user_id = %s"

# search user_id in blacklist table
search_blacklist = "SELECT * FROM Blacklist WHERE user_id = %s"

# add user_id to blacklist
add_to_blacklist = "INSERT INTO Blacklist VALUES (%s, UTC_DATE())"

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
new_project = "INSERT Projects VALUES (%s, %s, %s, %s, NULL, %s)"
add_pending_project = "INSERT PendingProjects VALUES (%s, %s, %s)"

# get user transaction history
get_transaction_history = "SELECT * FROM TransactionHistory WHERE sender = %s OR receiver = %s"

# remove project for testing purposes
remove_project = "DELETE FROM Projects WHERE project_id = %s"

# get project status
project_status = "SELECT project_status FROM Projects WHERE project_id = %s"

# get project type
project_type = "SELECT project_type FROM Projects WHERE project_id = %s"


#check if project name taken
project_exists = "SELECT project_id FROM Projects WHERE project_id = %s"

#place the team or individual bids
place_teambid = "INSERT Team_Bid_Project VALUES (%s, %s, %s)"
place_indivbid = "INSERT Individual_Bid_Project VALUES (%s, %s, %s)"

# get the project bids
individual_bids = "SELECT user_id, bid FROM Individual_Bid_Project WHERE project_id = %s ORDER BY bid ASC"
team_bids = "SELECT team_id, bid FROM Team_Bid_Project WHERE project_id = %s ORDER BY bid ASC"

# puts bid into current project table, also clears bid table of the project, same for individual chosen
choose_team_bid = "INSERT INTO Current_Team_Project VALUES (%s, %s, %s)"
choose_indiv_bid = "INSERT INTO Current_Individual_Project VALUES (%s, %s, %s)"

# gets all from current project record
get_current_team_project_info = "SELECT * FROM Current_Team_Project WHERE project_id = %s"
get_current_indiv_project_info = "SELECT * FROM Current_Individual_Project WHERE project_id = %s"

# puts current project into finished table
team_finished = "INSERT INTO Finished_Team_Project VALUES (%s, NULL, %s, NULL, %s)"
indiv_finished = "INSERT INTO Finished_Individual_Project VALUES (%s, %s, %s)"

# enters a review
make_project_review = "INSERT INTO TeamReviews VALUES (%s, %s, %s, %s, %s)"
