#ClassType class v0.1
#One instance for each kind of class offered at school, ex. academic grade 10 english, university grade 11 functions

import ClassUnit.ClassUnit

class ClassType:

	"""One ClassType object is created for each class offered at the school, including grade and stream versions. 
For example, grade 9 academic english or grade 12 university physics."""
	def __init__(self, courseCode, maxClassUnits):

		self.courseCode = courseCode
		self.maxClassUnits = maxClassUnits
		self.ClassUnits = []

	def addStudent(student):

		"""This method checks to see if there is space in a ClassUnit of the requested ClassType available, if so it adds the student. Otherwise it creates a
new ClassUnit if required, or returns False if impossible"""

		added = False

		for i in ClassUnits:

			added = i.addStudent(student)
		
		if added == False:

			if ClassUnits.len() < maxClassUnits:

				newClassUnit()
				i.addStudent(student)
				return True

			else:
				return False


	def newClassUnit():

		"""This method creates a new ClassUnit"""
		ClassUnit x = new ClassUnit
		self.ClassUnits.append(x)