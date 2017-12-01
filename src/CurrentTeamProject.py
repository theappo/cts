from Project import *

class CurrentTeamProject(Project):
	def __init__(self, project_id,client_id,description):
		super(CurrentTeamProject,self).__init__(project_id,client_id,description)

	# def get_assign_id():
	# 	db=GateWay()
	# 	return db.get_team(self.project_id)

# a=CurrentTeamProject(2,1,"hahaha")
# print(a.get_project_id(),a.get_client_id(),a.get_description())
