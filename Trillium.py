############################################
#EvilZone by Rafi Matchen and Anton Machula#
#Version 0.1				               #
############################################



while True:

	#For each grade, starting from grade 12
	for grade in grades:

		#Get student list from grade object
		students[] = grade.getStudents()

		# For each student in the grade
		for student in students:

			#Get students required corses and requested streams
			required = student.getRequired()


	#For each grade, starting from grade 12
	for grade in grades:

		#For each student in the grade
		for student in students:

			#Get students primary and alternate corse requests
			requests = student.getRequests()
			alternates = student.getAlternates()

			#Iterate through student requests 
			for request in requests:

				added = request.addStudent(student)
				
				if added == False:

					for alternate in alternates:

						added = classType.addStudent(student)

						if added == True:

							break