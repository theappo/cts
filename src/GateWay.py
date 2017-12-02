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

    # TODO: warning
    # TODO: get user warning number
    # add new user to users table, and application table ///Cool!
    def add_user(self, user_id, user_password, balance, user_type, user_email, user_address):
        if (self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(insert_user,
                                (user_id, user_password, int(user_type), float(balance), user_email, user_address))
            self.cursor.execute(insert_applications, user_id)  # might change this into a trigger
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # deletes user from system, (sets user to null in history)
    def delete_account(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(remove_user, user_id)
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

    # get user's type (0 = superuser, 1 = client, 2 = developer)
    def get_user_type(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_type, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data[0][0]

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

    # TODO: add reason to this function
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

    # return black reason and time
    def get_black_list(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(search_blacklist, user_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        return data


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

    # get blacklist reason


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

    # get clients as a list ordered by projects completed, limit size
    def get_active_clients(self, size=1):
        try:
            self.conn.connect()
            self.cursor.execute(active_client, size)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data

    # get devs as a list ordered by income, limit size
    def get_active_devs(self, size=1):
        try:
            self.conn.connect()
            self.cursor.execute(active_dev, size)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data

    # Project Methods
    def project_id_exists(self, project_name):
        try:
            self.conn.connect()
            self.cursor.execute(project_exists, project_name)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        if (len(data)):
            return True
        return False

    # gets project status (pending, current, or finished)
    def get_project_status(self, project_id):
        if (not self.project_id_exists(project_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(project_status, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0][0]

    # get project type (individual or team)
    def get_project_type(self, project_id):
        if (not self.project_id_exists(project_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(project_type, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0][0]

    # adds project to project table and pending project table
    def create_new_project(self, project_name, client_id, description, deadline, maxbid, bid_deadline):
        if (self.project_id_exists(project_name)):
            return False
        if (not (self.get_user_type(client_id) == 1)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(new_project, (project_name, client_id, description, "Pending", deadline))
            self.conn.commit()
            self.cursor.execute(add_pending_project, (project_name, float(maxbid), bid_deadline))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # deletes project id from system, should be used only for testing
    def delete_project(self, project_id):
        if (not self.project_id_exists(project_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(remove_project, project_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # place a team bid
    def place_team_bid(self, project_id, team_id, bid):
        if (not self.project_id_exists(project_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(place_teambid, (project_id, team_id, float(bid)))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # place individual bid
    def place_individual_bid(self, project_id, dev_id, bid):
        if (not self.project_id_exists(project_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(place_indivbid, (project_id, dev_id, float(bid)))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # returns the team bids as a list of lists for a pending project, add limit?
    def get_team_project_bids(self, project_id):
        if (not (self.get_project_status(project_id) == 'Pending')):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(team_bids, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # returns the individual bids as a list of lists, add limit?
    def get_individual_project_bids(self, project_id):
        if (not (self.get_project_status(project_id) == 'Pending')):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(individual_bids, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # choose a team_id's bid for a project, make sure team placed a bid!
    # trigger will clear other bids, and execute other necessary changes
    def choose_team(self, project_id, team_id, bid):
        if (not (self.project_id_exists(project_id))):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(choose_team_bid, (project_id, team_id, bid))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # choose a developer for a project, make sure dev placed a bid!
    # trigger will handle clearing other bids and other changes
    def choose_dev(self, project_id, dev_id, bid):
        if (not (self.project_id_exists(project_id))):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(choose_indiv_bid, (project_id, dev_id, bid))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # gets current team project info
    def get_current_team_project(self, project_id):
        if (not ((self.get_project_status(project_id) == "Current") and (self.get_project_type(project_id) == "Team"))):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_current_team_project_info, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_current_indiv_project(self, project_id):
        if (
                not (
                        (self.get_project_status(project_id) == "Current")(
                                self.get_project_type(project_id) == "Individual"))):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_current_indiv_project_info, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # project is finished, put in finished table, add ratings/reviews later?
    def finish_team_project(self, project_id):
        if (not ((self.get_project_status(project_id) == "Current") and (self.get_project_type(project_id) == "Team"))):
            return False
        data = self.get_current_team_project(project_id)
        try:
            self.conn.connect()
            self.cursor.execute(team_finished, (data[0][0], data[0][1], data[0][2]))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    def finish_individual_project(self, project_id):
        if (not ((self.get_project_status(project_id) == "Current") and (
                    self.get_project_type(project_id) == "Individual"))):
            return False
        data = self.get_current_indiv_project(project_id)
        try:
            self.conn.connect()
            self.cursor.execute(individual_finished, (data[0][0], data[0][1], data[0][2]))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # leave a project review, make it possible to replace one?
    # trigger will make sure 2 users were in project
    def create_project_review(self, project_id, sender, receiver, rating, message='NULL'):
        if (not (self.get_project_status(project_id) == "Finished")):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(make_project_review, (project_id, sender, receiver, message, rating))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True