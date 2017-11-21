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
			
	def check_blacklist(self, user_id):
		try:
			self.conn.connect()
			self.cursor.execute(search_blacklist, user_id)
			self.conn.close()
		except Exception as e:
			traceback.print_exc(e)

		data = self.cursor.fetchall()

		if(len(data)):
			return True
		else:
			return False

	def verify_user(self, user_id, password):
		try:
			self.conn.connect()
			self.cursor.execute(verify_user, (user_id, password))
			self.conn.close()
		except Exception as e:
			traceback.print_exc(e)

		data = self.cursor.fetchall()

		if(len(data)):
			return True
		else:
			return False


