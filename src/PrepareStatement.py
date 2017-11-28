# check is user_id exists
user_id_exists = "SELECT user_id from users where user_id = %s"

# insert new user
insert_user = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s)"

# insert user into dev table
insert_dev = "INSERT INTO developers VALUES (%s, 0)"

# insert user into client table
insert_client = "INSERT INTO clients VALUES (%s, 0)"

# remove user from application table
approve_user = "DELETE from application where user_id = %s"

# insert new user into applications too
insert_applications = "INSERT INTO application VALUES (%s)"

# search user_id in blacklist table
search_blacklist = "SELECT * FROM Blacklist WHERE user_id = %s"

# add user_id to blacklist

add_to_blacklist = "INSERT INTO Blacklist VALUES (%s, UTC_DATE())"

# search user_id and user_password in user table
verify_user = "SELECT user_type FROM users WHERE user_id = %s AND password = %s"

# get user_type
get_user_type = "SELECT user_type FROM users WHERE user_id = %s"

# test if username is taken
user_exists = "SELECT user_id FROM users WHERE user_id = %s"
# return user balance
user_balance = "SELECT balance FROM users where user_id = %s"
# set user balance
update_balance = "UPDATE users set balance = %s where user_id = %s"
# return user address
get_address = "SELECT address from users where user_id = %s"
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
active_client = "SELECT client_id from Projects group by client_id order by count(*) desc limit 1"

# get user transaction history
get_transaction_history = "SELECT * FROM TransactionHistory WHERE sender = %s OR receiver = %s"

