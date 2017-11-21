from Project import *

class FinishedTeamProject(Project):
	def __init__(self, project_id,client_id,description):
		super(FinishedTeamProject,self).__init__(project_id,client_id,description)

	# def get_assign_id():
	# 	db=GateWay()
	# 	return db.get_team(self.project_id)
	# def get_teamrating():
	# 	db=GateWay()
	# 	return db.get_team(self.project_id)

# a=FinishedTeamProject(2,1,"hahaha")
# print(a.get_project_id(),a.get_client_id(),a.get_description())
