# numbers = [1, 2, 3]
# new_list =[n + 1 for n in numbers]
# print(new_list)

# # list comprehension
# new_list = [new_item for number in numbers]

# # another one but if the test is true
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# # this will give you a new list of short_names and only add names less than 5 letters
# short_names = [name for name in names if len(name) < 5]
# # this will give you a new list with long names and all caps
# upper_names = [name.upper() for name in names if len(name) > 5]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above

# #Write your 1 line code 👇 below:

# result = [num for num in numbers if num%2==0]

# #Write your code 👆 above:

# print(result)

# with open("file1.txt", "r") as f:
#   file1_list = f.readlines()
# with open("file2.txt", "r") as f:
#   file2_list = f.readlines()
# result = [int(item) for item in file1_list if item in file2_list]
# # Write your code above 👆

# print(result)

#####

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Frank"]

# student_scores = {student:random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {key:value for (key, value) in student_scores.items() if value >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆

# # Write your code below:

# # each word as an item in a dictionary as key
# # count for each letter and add that to value

# result = {word:len(word) for word in sentence.split()}

# print(result)

#####

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆

# # Write your code 👇 below:
# # temp_f = (temp_c * 9/5) + 32

# weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}

# print(weather_f)

#####

# dict comprehension with data frames

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)
    print(key)

print("\n"*5)
import pandas

student_data_frame = pandas.DataFrame(student_dict)

for (key, value) in student_data_frame.items():
    print(value)

print("\n"*5)

for (index, rows) in student_data_frame.iterrows():
    print(rows)

for (index, row) in student_data_frame.iterrows():
    print(row.student)