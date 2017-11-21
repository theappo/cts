class Project():
	def __init__(self, project_id,client_id,description):

		self._project_id=project_id
		self._client_id=client_id
		self._description=description

	
	def get_project_id(self):
		return self._project_id

	def get_client_id(self):
		return self._client_id

	def get_description(self):
		return self._description

	# def get_project_status():
	# 	db=GateWay()
	# 	return db.get_project_status(project_id)
	# def get_project_type():
	# 	db=GateWay()
	# 	return db.get_project_type(project_id)

	# @abstractmethod
	# def get_assign_id():
	# 	pass


# a=Project(2,1,"hahaha")
# print(a.get_project_id(),a.get_client_id(),a.get_description())
 
	