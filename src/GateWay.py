#!/usr/bin/env python

""" GateWay.py: use to establish connection with mariadb server. """

import pymysql
import traceback

from PrepareStatement import *
from DatabaseInfo import *
from decimal import *


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

    # returns true if user is in applications list
    def check_application(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(user_approved, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        if (len(data) == 0):
            return False
        return True

    # get all applications for super user to approve/deny
    def get_applications(self):
        try:
            self.conn.connect()
            self.cursor.execute(get_applications)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data


    # remove user from application table
    def approve_user_id(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        if(self.check_blacklist(user_id)):
            self.deny_user_id(user_id, 'User_id on blacklist')
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

    # returns number of warnings
    def check_warning_number(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_warnings, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0][0]

    # super user removes warning from user
    def remove_warning(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(remove_warning, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # add user into blacklist
    def add_blacklist(self, user_id, reason):
        if (False and self.check_blacklist(user_id)):
            return False
        if (False and not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(add_to_blacklist, (user_id, reason))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        return True

    # delete user from blacklist
    def remove_blacklist(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(remove_from_blacklist, user_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

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
            return float(data[0][0])
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

    # get clients as a list ordered by projects completed, limit size
    def get_active_clients(self, size=3):
        try:
            self.conn.connect()
            self.cursor.execute(active_client, size)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data

    # get devs as a list ordered by income, limit size
    def get_active_devs(self, size=3):
        try:
            self.conn.connect()
            self.cursor.execute(active_dev, size)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()
        return data

    # update the user interests (default is all 0)
    def update_user_interests(self, user_id, Java, Python, Cpp, IOS, Android, Desktop):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(update_interests, (Java, Python, Cpp, IOS, Android, Desktop, user_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # returns user interests as array in order: Java, Python, C++, IOS, Android, Desktop
    def get_user_interests(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_user_interests, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()

        if len(data):
            return data[0]
        else:
            return (0, 0, 0, 0, 0, 0)

    # returns all user_ids ordered by most similar interests (should return less?)
    def get_similar_interests(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        data = self.get_user_interests(user_id)
        try:
            self.conn.connect()
            self.cursor.execute(find_similar_interests, (user_id, data[0], data[1], data[2], data[3], data[4], data[5]))
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # return user's average rating
    def average_rating(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_user_reviews, user_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        sum = 0
        count = 0
        for review in data:
            sum += review[4]
            count += 1
        if count != 0:
            return sum / count

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

    # gets all info from project record
    def get_project_info(self, project_id):
        if (not self.project_id_exists(project_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_project_info, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    # get clients pending projects (from projects join pendingprojects, includes projectid twice)
    def get_clients_pending_projects(self, client_id):
        if (not self.get_user_type(client_id) == 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_client_pending_projects, client_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # get clients current individual projects (from projects join indivprojects)
    def get_clients_current_indiv_projects(self, client_id):
        if (not self.get_user_type(client_id) == 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_client_current_indiv_projects, client_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # get clients current team projects
    def get_clients_current_team_projects(self, client_id):
        if (not self.get_user_type(client_id) == 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_client_current_team_projects, client_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # get clients finished indiv projects
    def get_clients_finished_indiv_projects(self, client_id):
        if (not self.get_user_type(client_id) == 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_clients_finished_indiv_projects, client_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # get clients finished team projects
    def get_clients_finished_team_projects(self, client_id):
        if (not self.get_user_type(client_id) == 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_clients_finished_team_projects, client_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # get dev's bids
    def get_devs_bids(self, dev_id):
        if (not self.get_user_type(dev_id) == 2):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_devs_bids, dev_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_devs_current_projects(self, dev_id):
        if (not self.get_user_type(dev_id) == 2):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_dev_current_projects, dev_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_devs_finished_projects(self, dev_id):
        if (not self.get_user_type(dev_id) == 2):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_dev_finished_projects, dev_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_devs_finished_team_projects(self, dev_id):
        if (not self.get_user_type(dev_id) == 2):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_dev_finished_team_projects, dev_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_team_bids(self, team_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_team_bids, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_team_current_projects(self, team_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_team_current_projects, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_team_finished_projects(self, team_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_team_finished_projects, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

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
    def create_new_project(self, project_name, client_id, description, deadline, maxbid , bid_deadline):
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

    def team_exists(self, team_id):
        try:
            self.conn.connect()
            self.cursor.execute(team_exists, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        if (len(data) > 0):
            return True
        return False

    def create_team(self, team_id, user_id):
        if (self.team_exists(team_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(create_team, (team_id, user_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    def get_team_devs(self, team_id):
        if (not self.team_exists(team_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_team_devs, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    def add_to_team(self, team_id, user_id):
        devs = self.get_team_devs(team_id)
        if (devs == False):
            return False
        if (devs[4] != None):
            return False
        size = 'dev5'
        if (devs[1] == None):
            size = 'dev2'
        elif (devs[2] == None):
            size = 'dev3'
        elif (devs[3] == None):
            size = 'dev4'
        if (devs[0] == user_id or devs[1] == user_id or devs[2] == user_id or devs[3] == user_id or devs[4] == user_id):
            return False

        try:
            self.conn.connect()
            if(size == 'dev5'):
                self.cursor.execute(add_to_team5, (user_id, team_id))
            elif(size == 'dev4'):
                self.cursor.execute(add_to_team4, (user_id, team_id))
            elif(size == 'dev3'):
                self.cursor.execute(add_to_team3, (user_id, team_id))
            elif(size == 'dev2'):
                self.cursor.execute(add_to_team2, (user_id, team_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    def remove_from_team(self, team_id, user_id):
        devs = self.get_team_devs(team_id)
        if (devs == False):
            return False
        size = 5
        i = 1
        if (devs[2] == None):
            size = 2
        elif (devs[3] == None):
            size = 3
        elif (devs[4] == None):
            size = 4
        if (devs[1] == None):
            return False
        if (devs[4] == user_id):
            i = 5
        elif (devs[3] == user_id):
            i = 4
        elif (devs[2] == user_id):
            i = 3
        elif (devs[1] == user_id):
            i = 2
        elif (devs[0] != user_id):
            return False
        query = 'set_team_devs' + str(i) + str(size)
        try:
            self.conn.connect()
            self.cursor.execute(query, (devs[size], team_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    def get_pending_projects(self):
        try:
            self.conn.connect()
            self.cursor.execute(get_pending_projects)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

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
        try:
            self.conn.connect()
            self.cursor.execute(individual_bids, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_lowest_bid(self, project_id):
        indivbid = self.get_individual_project_bids(project_id)
        teambid = self.get_team_project_bids(project_id)
        if(len(indivbid) == 0 and len(teambid) == 0):
            return -1
        if(len(indivbid) == 0):
            return teambid[0][1]
        if(len(teambid) == 0):
            return indivbid[0][1]
        if(indivbid[0][1] < teambid[0][1]):
            return indivbid[0][1]
        else:
            return teambid[0][1]

    # choose a team_id's bid for a project, make sure team placed a bid!
    # trigger will clear other bids, and execute other necessary changes
    def choose_team(self, project_id, team_id, bid):
        if (not (self.project_id_exists(project_id))):
            return False
        client = self.get_project_info(project_id)[1]
        funds = float(self.get_user_balance(client))
        if (11 / 10 * bid > funds):  # client can't afford
            return False
        team = self.get_teams_users(team_id)
        shares = 5
        if (team[1] == None):
            shares = 1
        elif (team[2] == None):
            shares = 2
        elif (team[3] == None):
            shares = 3
        elif (team[4] == None):
            shares = 4
        try:
            self.conn.connect()
            self.cursor.execute(choose_team_bid, (project_id, team_id, bid))
            for i in range(shares):
                self.cursor.execute(transferfunds1, (bid / shares / 2, team[i], project_id, project_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        self.update_user_balance(client, round(funds - bid / 2, 2))
        return True

    # choose a developer for a project, make sure dev placed a bid!
    # trigger will handle clearing other bids and other changes
    def choose_dev(self, project_id, dev_id, bid):
        if (not (self.project_id_exists(project_id))):
            return False
        client = self.get_project_info(project_id)[1]
        funds = float(self.get_user_balance(client))
        if (11 / 10 * bid > funds):  # client can't afford
            return False
        try:
            self.conn.connect()
            self.cursor.execute(choose_indiv_bid, (project_id, dev_id, bid))
            self.cursor.execute(transferfunds1, (bid / 2, dev_id, project_id, project_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        self.update_user_balance(client, round(funds - bid / 2, 2))

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
        return data[0]

    def get_current_indiv_project(self, project_id):
        if (
                not (
                        (self.get_project_status(project_id) == "Current") and(
                                self.get_project_type(project_id) == "Individual"))):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_current_indiv_project_info, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    # gets all from finished team project record
    def get_finished_team_project(self, project_id):
        if (self.get_project_status(project_id) != "Finished"):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_finished_team_project, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    # gets all from finished individual project record
    def get_finished_indiv_project(self, project_id):
        if (self.get_project_status(project_id) != 'Finished'):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_finished_indiv_project, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    # project is finished, put in finished table, add ratings/reviews later?
    def finish_team_project(self, project_id):
        if (not ((self.get_project_status(project_id) == "Current") and (self.get_project_type(project_id) == "Team"))):
            return False
        data = self.get_current_team_project(project_id)
        devs = self.get_project_teamdevs(project_id)
        client = self.get_project_info(project_id)[1]
        shares = 5
        if (devs[1] == None):
            shares = 1
        elif (devs[2] == None):
            shares = 2
        elif (devs[3] == None):
            shares = 3
        elif (devs[4] == None):
            shares = 4
        try:
            self.conn.connect()
            self.cursor.execute(team_finished, (data[0], data[1], data[2]))
            for i in range(shares):
                self.cursor.execute(transferfunds1, (data[2] / 2 / shares, devs[i], project_id, project_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        self.update_user_balance(client, Decimal(self.get_user_balance(client)) - data[2] / 2)
        return True

    def finish_individual_project(self, project_id):
        if (not ((self.get_project_status(project_id) == "Current") and (
                    self.get_project_type(project_id) == "Individual"))):
            return False
        data = self.get_current_indiv_project(project_id)
        try:
            self.conn.connect()
            self.cursor.execute(indiv_finished, (data[0], data[1], data[2]))
            self.cursor.execute(transferfunds1, (data[2] / 2, data[1], project_id, project_id))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        client = self.get_project_info(project_id)[1]
        self.update_user_balance(client, Decimal(self.get_user_balance(client)) - data[2] / 2)

        return True

    # leave a project review, make it possible to replace one?
    # trigger will make sure 2 users were in project
    def create_project_review(self, project_id, sender, receiver, rating, message='NULL'):
        if (sender == receiver):
            return False
        if (not (self.get_project_status(project_id) == "Finished")):
            return False
        if (not self.worked_on_project(sender, project_id)):
            return False
        if (not self.worked_on_project(receiver, project_id)):
            return False
        type = 'Individual'
        if (self.get_project_type(project_id) == 'Team'):
            type = 'Team'
        bid = 0
        if (self.get_project_type(project_id) == 'Team'):
            bid = self.get_finished_team_project(project_id)[4]
        else:
            bid = self.get_finished_indiv_project(project_id)[2]
        user = self.get_user_type(sender)
        try:
            self.conn.connect()
            self.cursor.execute(make_project_review, (project_id, sender, receiver, message, rating))
            print('review made')
            if (user == 1 and rating > 2 and type == 'Individual'):
                self.cursor.execute(transferfunds2, project_id)
                self.cursor.execute(canceltransfer, project_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        if (self.get_user_type(sender) == 1 and rating > 2 and type == 'Individual'):
            self.update_user_balance(sender, Decimal(self.get_user_balance(sender)) - bid / 20)
            self.update_user_balance(receiver, Decimal(self.get_user_balance(receiver)) + bid - bid / 20)
        return True

    def create_team_project_review(self, project_id, rating, message='NULL'):
        if (self.get_project_status(project_id) != 'Finished'):
            return False
        if (self.get_project_type(project_id) != 'Team'):
            return False
        bid = self.get_finished_team_project(project_id)[4]
        devs = self.get_project_teamdevs(project_id)
        client = self.get_project_info(project_id)[1]
        shares = 5
        if (devs[1] == None):
            shares = 1
        elif (devs[2] == None):
            shares = 2
        elif (devs[3] == None):
            shares = 3
        elif (devs[4] == None):
            shares = 4
        for i in range(shares):
            self.create_project_review(project_id, client, devs[i], rating, message)
            self.update_user_balance(devs[i], Decimal(self.get_user_balance(devs[i])) + bid - bid / 20 / shares)
            self.update_user_balance('SuperUser', Decimal(self.get_user_balance('SuperUser')) + bid / 20 / shares)
        self.update_user_balance(client, Decimal(self.get_user_balance(client)) - bid / 20)
        self.update_user_balance('SuperUser', Decimal(self.get_user_balance('SuperUser')) + bid / 20)
        try:
            self.conn.connect()
            self.cursor.execute(make_team_project_review, (rating, message, project_id))
            if (rating > 2):
                for i in range(shares):
                    self.cursor.execute(transferfunds2, project_id)
                    self.cursor.execute(canceltransfer, project_id)
                    self.cursor.execute(add_transaction, (bid / 20 / shares, 'SuperUser', devs[i]))
                self.cursor.execute(add_transaction, (bid / 20, 'SuperUser', client))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

    # return all projects where client gave review < 3 and transaction isnt approved yet
    def get_bad_projects(self):
        try:
            self.conn.connect()
            self.cursor.execute(get_bad_projects)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # super user sets dev(s) ratings and cost.
    def settle_project_dispute(self, project_id, new_rating, new_cost):
        try:
            self.conn.connect()
            self.cursor.execute(update_team_review, (new_rating, project_id))
            self.cursor.execute(update_team_project_review, (new_rating, new_cost, project_id))
            self.cursor.execute(update_indiv_project_review, (new_cost, project_id))
            self.cursor.execute(canceltransfer, project_id)
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        project_info = self.get_project_info(project_id)
        if (project_info[4] == 'Individual'):
            dev = self.get_finished_indiv_project(project_id)[1]
            self.transfer_funds(project_info[1], dev, new_cost)
            self.transfer_funds(project_info[1], 'SuperUser', new_cost / 20)
            self.tranfer_funds(dev, 'SuperUser', new_cost / 20)
        else:
            devs = self.get_project_teamdevs(project_id)
            size = 5
            if (devs[1] == None):
                size = 1
            elif (devs[2] == None):
                size = 2
            elif (devs[3] == None):
                size = 3
            elif (devs[4] == None):
                size = 4
            for i in range(size):
                self.transfer_funds(project_info[1], devs[i], new_cost / size)
                self.transfer_funds(devs[i], 'SuperUser', new_cost / size / 20)
            self.transfer_funds(project_info[1], 'SuperUser', new_cost / 20)
        return True

    def worked_on_project(self, dev_id, project_id):
        if (self.get_project_status(project_id) != 'Finished'):
            return False
        client = self.get_project_info(project_id)[1]
        if (client == dev_id):
            return True
        if(self.get_project_type(project_id) == 'Team'):
            devs = self.get_project_teamdevs(project_id)
            if (dev_id == devs[0] or dev_id == devs[1] or dev_id == devs[2] or dev_id == devs[3] or dev_id == devs[4]):
                return True
        elif(self.get_project_type(project_id) == 'Individual'):
            return (self.get_finished_indiv_project(project_id)[1] == dev_id)
        return False

    def get_inbox_message(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(inbox_message, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        return data

    def get_sent_message(self, user_id):
        try:
            self.conn.connect()
            self.cursor.execute(sent_message, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

        data = self.cursor.fetchall()

        return data

    def new_message(self, sender, receiver, message):
        try:
            self.conn.connect()
            self.cursor.execute(new_message, (sender, receiver, message))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)

            # Search functions

    def search_by_user_id(self, user_id):
        user_id = '%' + user_id + '%'
        try:
            self.conn.connect()
            self.cursor.execute(search_users, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def search_by_team_id(self, team_id):
        team_id = '%' + team_id + '%'
        try:
            self.conn.connect()
            self.cursor.execute(search_teams, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def search_by_indivprojectid(self, project_id):
        project_id = '%' + project_id + '%'
        try:
            self.conn.connect()
            self.cursor.execute(search_indiv_finished_projects, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def search_by_teamprojectid(self, project_id):
        project_id = '%' + project_id + '%'
        try:
            self.conn.connect()
            self.cursor.execute(search_team_finished_projects, project_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # gets the 5 devs on the team that completed a project
    def get_project_teamdevs(self, project_id):
        projectinfo = ''
        if (self.get_project_status(project_id) == "Finished"):
            projectinfo = self.get_finished_team_project(project_id)
            projectinfo = [projectinfo[2], projectinfo[5]]
        elif (self.get_project_status(project_id) == "Current"):
            projectinfo = self.get_current_team_project(project_id)
            projectinfo = [projectinfo[1], 'NOW()']
        try:
            self.conn.connect()
            if (projectinfo[1] == 'NOW()'):
                self.cursor.execute(get_project_teamdevs2, projectinfo[0])
            else:
                self.cursor.execute(get_project_teamdevs, (projectinfo[0], projectinfo[1]))
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    # gets all of team's projecthistory
    def get_team_projecthistory(self, team_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_teamhistory, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # gets all of users projectreviews
    def get_projectreviews(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_user_reviews, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # get all of users teams
    def get_users_teams(self, user_id):
        if (not self.user_exists(user_id)):
            return False
        if (self.get_user_type(user_id) != 2):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_users_teams, (user_id, user_id, user_id, user_id, user_id))
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    # gets all of teams users
    def get_teams_users(self, team_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_teams_users, team_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data[0]

    # checks if client's project deadline has passed
    def check_client_projects(self, user_id):
        if (self.get_user_type(user_id) != 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_client_overdue_projects, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        for project in data:
            self.delete_project(project[0])
            self.transfer_funds(user_id, 'SuperUser', 10.00)
        return True

    # checks for late devs/teams
    def check_client_projects2(self, user_id):
        if (self.get_user_type(user_id) != 1):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_client_overdue_projects2, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()

        for project in data:
            if (self.get_project_type(project[0]) == 'Individual'):

                self.finish_individual_project(project[0])
                project_info = self.get_finished_indiv_project(project[0])[0]
                self.transfer_funds(projectinfo[1], user_id, projectinfo[2] / 10)
                try:
                    self.conn.connect()
                    self.cursor.execute(canceltransfer, project[0])
                    self.cursor.excecute(make_project_review, (project[0], project_info[1], user_id, 'Late Project', 1))
                    self.conn.commit()
                    self.conn.close()
                except Exception as e:
                    traceback.print_exc(e)
            if (self.get_project_type(project[0]) == 'Team'):
                self.finish_team_project(project)
                project_info = self.get_finished_team_project(project[0])[0]
                devs = self.get_project_teamdevs(project[0])
                shares = 5
                if (devs[1] == None):
                    shares = 1
                elif (devs[2] == None):
                    shares = 2
                elif (devs[3] == None):
                    shares = 3
                elif (devs[4] == None):
                    shares = 4
                for i in range(shares):
                    self.transfer_funds(devs[i], user_id, project_info[4] / shares / 10)
                try:
                    self.conn.connect()
                    self.cursor.execute(canceltransfer, project[0])
                    self.cursor.execute(make_team_project_review, (1, 'Late Project', project[0]))
                    self.conn.commit()
                    self.conn.close()
                except Exception as e:
                    traceback.print_exc(e)
                for i in range(shares):
                    self.create_project_review(project[0], user_id, devs[i], 1, 'Late Project')
        return True

    def get_dev_pending_client_reviews(self, user_id):
        if (not self.get_user_type(user_id) == 2):
            return False
        try:
            self.conn.connect()
            self.cursor.execute(get_dev_pending_client_reviews, user_id)
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        return data

    def get_dev_pending_reviews(self, user_id, project_id):
        if (not self.get_project_status(project_id) == 'Finished'):
            return False
        if (self.get_user_type(user_id) != 2):
            return False
        project_info = self.get_project_info(project_id)
        devs = ''
        if (project_info[4] == 'Team'):
            devs = self.get_project_teamdevs(project_id)
        data = []
        if (self.get_review(project_id, user_id, project_info[1]) == False):
            data = data + [[project_id, project_info[1]]]
        if(self.get_project_type(project_id) == 'Team'):
            size = 5
            if (devs[1] == None):
                size = 1
            elif (devs[2] == None):
                size = 2
            elif (devs[3] == None):
                size = 3
            elif (devs[4] == None):
                size = 4
            for i in range(size):
                if (devs[i] == user_id):
                    continue
                if (self.get_review(project_id, user_id, devs[i]) == False):
                    data = data + [[project_id, devs[i]]]
        return data

    # gets specific review
    def get_review(self, project_id, sender_id, receiver_id):
        try:
            self.conn.connect()
            self.cursor.execute(get_review, (sender_id, receiver_id, project_id))
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        data = self.cursor.fetchall()
        if (len(data) == 0):
            return False
        return data[0]

    def transfer_funds(self, sender, receiver, amount):
        self.update_user_balance(sender, Decimal(self.get_user_balance(sender)) - Decimal(amount))
        self.update_user_balance(receiver, Decimal(self.get_user_balance(receiver)) + Decimal(amount))
        try:
            self.conn.connect()
            self.cursor.execute(add_transaction, (amount, receiver, sender))
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            traceback.print_exc(e)
        return True

#db = GateWay()
#print(db.finish_individual_project(1))
