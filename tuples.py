# # Exercises on tuples

# sisters = ("Mary", "Anna", "Kate", "Martha", "Sarah")
# brothers = ("John", "Paul", "George", "Ringo", "James")
# siblings = sisters + brothers
# print(siblings)  # Concatenate sisters and brothers
# print(len(siblings))  # Length of siblings tuple
# parent = ("John", "Mary")
# family_members = siblings + parent  # Concatenate siblings and parent
# print(family_members)  # Print family members

# family_members = (family_members)  # Convert tuple to list
# parent = ("John", "Mary")
# sisters = ("Mary", "Anna", "Kate", "Martha", "Sarah")
# parent, sisters = family_members


#Creating a tuple of fruits,vegetables and animals
fruits = ("apple", "banana", "cherry", "orange", "grape")
vegetables = ("carrot", "broccoli", "spinach", "potato", "tomato")
animals = ("dog", "cat", "elephant", "tiger", "lion")
food_stuff_tp= fruits + vegetables + animals
print(food_stuff_tp)  # Print all fruits, vegetables, and animals

food_stuff_lt= list(food_stuff_tp)  # Convert tuple to list

#slicing the middle item from the list
middle_index = len(food_stuff_lt) // 2  # Calculate the middle index
middle_item = food_stuff_lt[middle_index]  # Get the middle item
print(middle_item)  # Print the middle item
#sicing the first three items and the last three items
first_three_items= food_stuff_lt[:3]
last_three_items= food_stuff_lt[-3:]
food_items= first_three_items + last_three_items  # Concatenate first and last three items
print(food_items)  # Print the first three and last three items

#deleting a tuple
del food_stuff_tp

#checking to see if an items is in the tuple
print("apple" in food_stuff_tp)  # Check if "apple" is in the tuple

