#Creating of a dictionary of dogs
dog = {
    "name" :"Jackie",
    "color" : "Brown",
    "legs" :"Four",
    "age" : 4,
}
print(dog)

#Creating a dictionary of student
dict_student = {
    "first_name":"Marlene",
    "last_name" :  "Quist",
    "gender": "female",
    "age": 24,
    "marital status":"single",
    "skill":{"Java,SQL,Django"},
    "country":"Japan",
    "city":"Tokyo",
    "address" : {
        "Street": "Beach Drive",
    }
}
print(dict_student)
#Lenght of Dictionary
print(len(dict_student))
#GEt function of dictionary
get_skill = dict_student.get("skill")
print(get_skill)

#Modifying Skills dictionary
dict_student["skill"]= "Python,React",
print(dict_student)

#Adding new key to the dictionary   
dict_student["hobby"] = "Reading",  
print(dict_student) 

#getting keys as list
keys=dict_student.keys()
print(keys)

#Getting values as list
values=dict_student.values()
print(values)

#deleting an item from the dictionary   
del dict_student["hobby"]       
print(dict_student)

#deleting a key from the dictionary using pop() method
dict_student.pop("age") 
print(dict_student)