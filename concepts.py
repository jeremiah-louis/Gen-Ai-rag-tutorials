# # First class functions
# dictionary_for_users_and_budgets = {
#     "Alice": {
#         "Dining Out": 120,
#         "Entertainment": 80,
#         "Groceries": 150,
#         "Health & Fitness": 50,
#         "Utilities": 60,
#     },
# }
# # variable declarations
# username = dictionary_for_users_and_budgets.get("Alice")

# def expense_tracker(expense,func):
#     """returns the specific rewards based on expense"""
#     return func(expense)

# def cash_back(expense):
#     """returns a 5% cashback after dining out expenses crosses $50"""
#     if expense["Dining Out"] > 50:
#         return expense["Dining Out"] * (5 / 100)
#     else:
#         return "You have no cashback points"


# def budget_limit(expense):
#     """returns an alert that expenses in the entertainment exceed $100"""
#     if expense.get("Entertainment") > 100:
#         return f"Yoo! How far blood na so the movie interesting small small!. \n You have spent {expense.get("Entertainment")} on netflix oh"
#     else:
#         return "Thats very good bro! keep it up"


# def reward_points(expense):
#     """returns a point value when health and fitness expenses exceed $50"""
#     point_value = 5
#     if expense.get("Health & Fitness") >= 50:
#         return f"You have been awarded {point_value} points. Keep at it "
#     else:
#         return f"Bro you fat oh ah ah try reduce small "

# print(expense_tracker(username,cash_back))
# print(expense_tracker(username,reward_points))


# HangmanGame

# import random


# list_of_words = [
#     "apple",  # 5 letters
#     "banana",  # 6 letters
#     "cherry",  # 6 letters
#     "date",  # 4 letters
#     "elderberry",  # 10 letters
#     "fig",  # 3 letters
#     "grape",  # 5 letters
#     "honeydew",  # 8 letters
#     "kiwi",  # 4 letters
#     "lemon",
# ]


# def hidden_underscores():
#     """loops through the list and abstracts each character"""
#     variable = []
#     for words in list_of_words:
#         formatted_word = "".join([_ for _ in words])
#         variable = [x for x in formatted_word].append()
#     return print(variable)


# hidden_underscores()


# def randomise_list(func):
#     random.shuffle(func)


# randomise_list()


# def create_html_element(tag):

#     def create_word_wrap(msg):
#         print(f"<{tag}> {msg} </{tag}>")

#     return create_word_wrap


# create_tag = create_html_element("h1")
# create_tag("hello")


# def create_html_tag(tag):
#     return lambda msg: print(f"<{tag}> {msg} </{tag}>")


# tag = create_html_tag("h1")
# tag("hello Jerry")
# tag("hello christabel")
# num_list = [2, 3, 4, 5, 6]


# def square_list(my_list):

#     def operator():
#         return [numbers**3 for numbers in my_list]

#     return operator


# result = square_list(num_list)


# print(result())
x = int(input())
y = int(input())
z = int(input())
n = int(input())
# storage_container = []
# for i in [x, y, z]:
#     for j in [x, y, z]:
#         for k in [x, y, z]:
#             storage_container.append([i, j, k])
# print(storage_container)

lis = [
    [x, y, z]
    for x in range(x + 1)
    for y in range(y + 1)
    for z in range(z + 1)
    if x + y + z != n
]
print(lis)
