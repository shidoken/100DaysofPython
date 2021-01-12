# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# with open("./NATO-alphabet-start/nato_phonetic_alphabet.csv", "r") as a:
#     alpha = a.readlines()
#     alpha = [code.strip() for code in alpha]
#     alpha = {i[0]:i[2:] for i in alpha if i != "letter,code"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# stop = True
# while stop:
#     code = input("What's your name? ").upper()
#     code = [alpha[char] for char in code]
#     print(code)
#     check = input("Try another?: ").lower()
#     if check == "n" or "no":
#         stop = False
#     else:
#         continue


import pandas
data = pandas.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# print(dictionary)

word = input("Enter a word: ").upper()
output = [dictionary[letter] for letter in word]
print(output)