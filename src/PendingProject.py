from Project import *

class PendingProject(Project):
	def __init__(self, project_id,client_id,description):
		super(PendingProject,self).__init__(project_id,client_id,description)

# a=PendingProject(2,1,"hahaha")
# print(a.get_project_id(),a.get_client_id(),a.get_description())
