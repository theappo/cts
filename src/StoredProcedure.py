# search user_id in blacklist table
search_blacklist = "SELECT * FROM blacklist WHERE user_id = %s"

# search user_id and user_password in user table
verify_user = "SELECT * FROM users WHERE user_id = %s AND password = %s"