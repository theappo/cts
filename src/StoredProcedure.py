# search user_id in blacklist table
search_blacklist = "SELECT * FROM blacklist WHERE user_id = %s"

# search user_id and user_password in user table
verify_user = "SELECT user_type FROM users WHERE user_id = %s AND password = %s"


user_exists = "SELECT * FROM users WHERE user_id = %s"

user_balance = "SELECT balance FROM users where user_id = %s"

return_resume = 