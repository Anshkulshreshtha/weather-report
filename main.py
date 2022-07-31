# # Method 1 with the general open keyword
#
# # with open("weather_data.csv") as Data:
# #     for data in Data:
# #         info = Data.readline()
# #         print(info)
#
#
# # Method 2 become more better with the use of csv module
#
# # import csv
# #
# # with open("weather_data.csv") as Data:
# #     Info = csv.reader(Data)
# #     temperature = []
# #     for info in Info:
# #         print(info)
# #         if info[1] != "temp":
# #             temperature.append(int(info[1]))
# #     print(temperature)
#
#
# #  Method 3 become more and more better with the use of PANDAS library
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# # data_list = data["temp"].to_list()
# # print(data_list)
# # Total_temp = 0
# # for temp in data["temp"]:
# #     Total_temp += temp
# # Average_temp = Total_temp / len(data["temp"])
# # print(Average_temp)
# #
# # print(data["temp"].max())
# #
# # # getting data in row
# #
# # print(data[data.day == "Monday"])
# # print(data[data.day == "Thursday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# temp_faranhiet = ((monday_temp) * 9/5) + 32
#
# print(f"The temp in Faranhiet is {temp_faranhiet}")


# data analysis of squirrel census data

import pandas

Data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_squirrel_count = len(Data[(Data["Primary Fur Color"] == "Gray")])
Cinnamon_squirrel_count = len(Data[(Data["Primary Fur Color"] == "Cinnamon")])
Black_squirrel_count = len(Data[(Data["Primary Fur Color"] == "Black")])

data_dict = {
    "Fur_color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray_squirrel_count, Cinnamon_squirrel_count, Black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
