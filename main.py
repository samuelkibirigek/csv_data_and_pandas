# """Option 1: The longest(least efficient) approach
# using the basic file manipulation"""
#
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# #I wont go ahead to complete option one assuming you get the idea.
#
#
# """Option 2: The longer(less efficient) approach
# using csv inbuilt library import"""
#
# import csv
#
# temperature = []
# temp = []
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     for row in data:
#         if row != "temp":
#             temp.append(row[1])
#
# for _ in temp[1:]:
#     temperature.append(int(_))
#
# print(temperature)
#

"""Option 3: USING PANDAS"""
import pandas

temperature = []
data = pandas.read_csv("weather_data.csv")

temperature.append(data["temp"])
print(temperature)






