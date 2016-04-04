from random import randint

firstName = []
lastName = []
fullName =[]


#The below code will just pull first and and last name files into an array

with open('firstNames','r') as f:
    for line in f:
        for word in line.split():
           print(word)      
           firstName.append(word)

with open('lastNames','r') as f:
    for line in f:
        for word in line.split():
           print(word)
           lastName.append(word)      

for i in range(1000):
	n = randint(1,len(lastName))
	n-=1
	m = randint(1,len(firstName))
	m-=1

#There will be five arrays, name, id, comlusory, alternate

	print "%s %s" %(firstName[m], lastName[n])
	fullName.append("%s %s" %(firstName[m], lastName[n]))


