import csv
import Student

studentList = []


data = 'data.csv'

with open(data, 'rb') as f:
    try:
    reader = csv.reader(f)
        for row in reader:
        	studentList.append(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

for i in studentList:
	Student(i)
	