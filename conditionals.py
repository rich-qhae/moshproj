# #Conditions is day 9
user_age = input("Enter your age: ")
if int(user_age) >= 18:
    print("You can drive")
else:
    secondary_age = 18 - int(user_age)
    print("You need to wait", secondary_age, "years to drive")

# #Getting two inputs from the user and comparing which one is greater
num1 = input("Enter first number: ")    
num2 = input("Enter second number: ")
if int(num1) > int(num2):
    print(num1, "is greater than", num2)
elif int(num1) < int(num2):
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

#Writing codes to grade students based on their scores
score = input("Enter your score: ")
if int(score)>= 80 and int(score)<= 100:
    print("You got A")
elif int(score)>= 70 and int(score)< 79:
    print("You got B")
elif int(score)>= 60 and int(score)< 69:       
    print("You got C")
elif int(score)>= 50 and int(score)< 59:    
    print("You got D")  
elif int(score)>= 0 and int(score)< 49:
    print("You got F")
else:
    print("Invalid score")  

#CHECKING THE SEASONS OF THE YEAR
month = input("Enter the month: ")
if month == "January" or month == "February" or month == "December":
    print("It is Winter")
elif month == "April" or month == "May" or month == "March": 
    print("It is Spring")
elif month == "July" or month == "August" or month == "June":
    print("It is Summer")
elif month == "October" or month == "November" or month == "September":
    print("It is Autumn")
else:
    print("Invalid month")


fruit = input("What fruit do you have: ")

fruits = ['banana', 'orange', 'mango', 'lemon']

if fruit in fruits:
    print(f"{fruit} is already in the list.")
else:
    fruits.append(fruit)
    print(f"{fruit} has been added to the list.")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


# Getting the middle skills
skills = person['skills'][2:]

if len(skills) > 0:
    print("Middle skills:", skills)

# Checking for specific skills
if 'Python' in person['skills']:
    print("You know Python")

elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print("You are a frontend developer")

if 'MongoDB' in person['skills'] and 'Node' in person['skills']:
    print("You are a backend developer")

else:
    print("No title")

if person['is_marred']:
    print("You are married")
else:   
    print("You are not married")