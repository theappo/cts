#!/usr/bin/env python

""" GateWay.py: use to establish connection with mariadb server. """

import pymysql
import traceback

from PrepareStatement import *
from DatabaseInfo import *


class GateWay(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(db=db_name,
                                        user=db_user,
                                        passwd=db_passwd,
                                        host=db_host,
                                        port=db_port)
            self.cursor = self.conn.cursor()
        except Exception as e:
            traceback.print_exc(e)
        finally:
            self.conn.close()

    # check if username is taken
    def user_exists(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(user_id_exists, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        if (len(data)):
            return True
        else:
            return False

    # add new user to users table, and application table
    def add_user(self, user_id, user_password, balance, user_type, user_email, user_address):
        if (self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(insert_user,
                                (user_id, user_password, int(user_type), float(balance), user_email, user_address))
            self.cursor.execute(insert_applications, user_id)
            if (user_type == 1):
                self.cursor.execute(insert_client, user_id)
            if (user_type == 2):
                self.cursor.execute(insert_dev, user_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # remove user from application table
    def approve_user_id(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(approve_user, user_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # check if username is in blacklist
    def check_blacklist(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(search_blacklist, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        if (len(data)):
            return True
        else:
            return False

    # add user into blacklist
    def add_blacklist(self, user_id):
        if (False and self.check_blacklist(user_id)):
            return False
        if (False and not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(add_to_blacklist, user_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # check if user entered correct user_id and password
    def verify_user(self, user_id, password):
        try:
            self.conn.connect()
            self.cursor.execute(verify_user, (user_id, password))
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        if (len(data)):
            return True
        else:
            return False

    # check user type
    def user_type(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_type, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        return data[0][0]

    # get user's account balance
    def get_user_balance(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(user_balance, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        if (len(data)):
            return data[0][0]
        else:
            return False

    # set user's account balance
    def update_user_balance(self, user_id, new_balance):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(update_balance, (float(new_balance), user_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # clear all blacklist entries, use for testing only
    def clear_blacklist(self):
        try:
            self.conn.connect()
            self.cursor.execute("delete from Blacklist")
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # get user's address
    def get_user_address(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_address, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data[0][0]

    # set user's address
    def set_user_address(self, user_id, new_address):
        if (not self.user_exists(user_id)):
            return False

        try:
            self.conn.connect()
            self.cursor.execute(update_address, (new_address, user_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # set user's password
    def set_user_password(self, user_id, new_password):
        if (not self.user_exists(user_id)):
            return False

        try:
            self.conn.connect()
            self.cursor.execute(update_password, (new_password, user_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # get user's email address
    def get_user_email(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_email, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data[0][0]

    # set user's email address
    def set_user_email(self, user_id, new_email):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(update_email, (new_email, user_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # get user's transaction history
    def get_transaction_history(self, sender, receiver):
        try:
            self.conn.connect()
            self.cursor.execute(get_transaction_history, (sender, receiver))
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        return data


    # returns number of developers registered
    def get_dev_num(self):
        try:
            self.conn.connect()
            self.cursor.execute(count_devs)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data[0][0]

    # returns number of clients registered
    def get_client_num(self):
        try:
            self.conn.connect()
            self.cursor.execute(count_clients)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data[0][0]

    # get client with most projects (history and active)
    def get_active_client(self):
        try:
            self.conn.connect()
            self.cursor.execute(active_client)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data[0][0]
