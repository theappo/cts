# check is user_id exists
user_id_exists = "SELECT user_id from users where user_id = %s"

# insert new user
insert_user = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"

# remove user from application table
approve_user = "DELETE from application where user_id = %s"

# remove user from system (foreign keys will cascade)
remove_user = "DELETE from users where user_id = %s"

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
user_balance = "SELECT balance FROM users where user_id = %s"

# set user balance
update_balance = "UPDATE users set balance = %s where user_id = %s"

# return user address
get_address = "SELECT address FROM users where user_id = %s"

# set user address
update_address = "UPDATE users set address = %s where user_id = %s"

# set user password
update_password = "UPDATE users set password = %s where user_id = %s"

# get user email
get_email = "SELECT email from users where user_id = %s"

# set user email
update_email = "UPDATE users set email = %s where user_id = %s"

# count number of devs
count_devs = "SELECT count(*) from Developers"

# count number of clients
count_clients = "SELECT count(*) from Clients"

# get client with most projects
active_client = "SELECT client_id from Projects group by client_id order by count(*) desc limit %s"

# gets the dev with most income in transaction history (iterating through projects would take longer / more work)
active_dev = "SELECT receiver from transactionhistory where receiver in (SELECT user_id from users where user_type = 2) group by receiver order by SUM(amount) desc limit %s"

# Create a project (must insert to projects and pendingprojects)
new_project = "INSERT Projects VALUES (%s, %s, %s, %s, NULL, %s)"
add_pending_project = "INSERT PendingProjects VALUES (%s, %s, %s)"

#check if project name taken
project_exists = "SELECT project_id from Projects where project_id = %s"
