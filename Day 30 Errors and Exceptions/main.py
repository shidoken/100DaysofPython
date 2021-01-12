# FileNotFound
# with open("a_file.txt", "r") as file:
#     file.read()

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary['non_existent_key']

#TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something')
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

## 30.1 IndexError Handling

# fruits = ["apple", "pear", "orange"]

# #TODO: Catch the exception and make sure the code
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print("Fruit pie")

# make_pie(1)

