class  (ClassUnit):
	"""One ClassUnit object is created for each INDIVIDUAL class, for example if there are two grade 11 physics, then two 
ClassUnit objects are created."""

	def __init__(self, capacity):
		self.capacity = capacity
		self.studentList = []

	def addStudent(student):

		if self.studentList.len() < self.capacity:
			self.studentList.append(student)
			return True
		else:
			return False