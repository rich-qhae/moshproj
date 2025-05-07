#day 7 sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Finding the lenght od the set it_companies
print(f"Length of it_companies set is: ", len(it_companies))

#adding an item "Twitter" to the set it_companies
it_companies.add("Twitter")
print(it_companies)

#removing an item from it_companies
it_companies.remove("IBM") # Remove "IBM" from the set and takes arguements
print(it_companies)

it_companies.pop()  # Remove an arbitrary element from the set Pop method takes no arguments and takes the first element of the set
print(it_companies)

#the difference betwwen remove and discard method:
#Remove method will raise an error if item is not found in set
# Discard method will not raise an error if item is not found in set
# Example: 
#it_companies.remove("NonExistent")  # Raises KeyError if "NonExistent" is not in the set
#it_companies.discard("NonExistent")  # Does not raise an error if "NonExistent" is not in the set

#Joining A and B
C = A.union(B)  # Update A with elements from B
print(C)

#finding intersection of A and B
 
D = A.intersection(B)  # Find common elements between A and B
print(D)

#Finding if A is subset of B
is_subset = A.issubset(B)  # Check if A is a subset of B
print(is_subset)    

is_disjoint = A.isdisjoint(B)  # Check if A and B have no common elements   
print(is_disjoint)

#joining A and B and B and A
E = A.union(B)  # Join A and B
print(E)

#symmetric difference of A and B
F = A.symmetric_difference(B)  # Find elements in A or B but not both
print(F)

#deleting a set completely
del A  # Delete set A   
del B  # Delete set B

#converting the list to set
age_set=set(age)  # Convert list to set
print(age_set)  # Print the set of ages

#comparing to see which has a longer lenght
lenght_set = len(age_set)  # Length of the set
lenght_list = len(age)  # Length of the list
print(lenght_set)  # Print the length of the set
print(lenght_list)  # Print the length of the list 

#the length of the set is smaller because it removes duplicates whilst the list doesn't

#Comparing the length of the set and the list
if len(set(age)) > len(age):
    print("fuck!!!")
else:
    print("Erhn")
