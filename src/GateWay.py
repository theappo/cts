#!/usr/bin/env python

"""GateWay.py: use to establish connection with mariadb server."""

import pymysql
import traceback

from StoredProcedure import *
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
			

	def vaild_user(self, user_id):
		try:
			self.conn.connect()
			self.cursor.execute(vaild_user_id, user_id)
			self.conn.close()
		except Exception as e:
			traceback.print_exc(e)
		#clone all row from cursor
		data = self.cursor.fetchall()
		if(len(data)):
			return True
		else:
			return False


