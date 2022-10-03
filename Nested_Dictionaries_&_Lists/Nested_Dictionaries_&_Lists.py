# # Update Values in Dictionaries and Lists

# x = [[5, 2, 3], [10, 8, 9]]

# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]

# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }

# z = [{'x': 10, 'y': 20}]


# x[1][0] = 15
# print(x)

# students[1]['last_name'] = 'Bryant'
# print(students)

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# z[0]['y'] = 30
# print(z)

# Iterate Through a List of Dictionaries
# Create a function iterateList(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


# def iterateList(some_list):
#     for i in range(0, len(some_list)):
#         print(
#             f"Student Number {i+1} - {some_list[i]['first_name']} {some_list[i]['last_name']}")


# iterateList(students)

# Agnostic Version

# def iterateList2(key_value, some_list):
#     for i in range(0, len(some_list)):
#         print(
#             f"{some_list[i][key_value]}")


# iterateList2('first_name', students)
# print()
# iterateList2('last_name', students)
