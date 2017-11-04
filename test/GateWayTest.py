#!/usr/bin/python3
import os

from GateWay import *

def main():

	Manager = GateWay()

	print(Manager.vaild_user('if'))

	print(Manager.vaild_user('testuser2'))

main()