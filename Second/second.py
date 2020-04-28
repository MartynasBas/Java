import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient["mydb"]

mycol = mydb["restaurants"]

def q1():
	for row in mycol.find():
	  print(row)

def q2():
	for row in mycol.find({},{ "restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1 }):
		print(row)

def q3():
	for row in mycol.find({},{ "_id" : 0,"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1 }):
		print(row)

def q4():
	for row in mycol.find({"borough": "Bronx"}):
		print(row)

def q5():
	for row in mycol.find({"grades": { "$elemMatch": { "score": { "$gte": 80, "$lte": 100 } } } } ):
		print(row)



#q1()
#q2()
#q3()
#q4()
q5()