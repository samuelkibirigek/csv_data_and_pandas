import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg = sum(temp_list) / len(temp_list)
# print(round(avg, 1))

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp_F = ((monday.temp * 1.8) + 32)

print(f"the temperature in Fahrenheit is {temp_F}")

