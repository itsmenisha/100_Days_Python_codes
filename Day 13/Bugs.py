
############ DEBUGGING#####################

# 1.Describe Problem
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#             # this only gors upto 19 so write 21
# my_function()

# # 2.Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # this has six strings
# dice_num = randint(0,5)
# # this goes from 1 to 6 and the list is supposed to start at 0 to 5
# print(dice_imgs[dice_num])


# 3. Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1994:
#     print("You are a Gen Z.")
# elif year > 1980 and year < 1994:
#     print("You are a millenial.")


# 4. Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# 5. Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# 6. Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
# mutate([1, 2, 3, 5, 8, 13])
