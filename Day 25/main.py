# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temprature = []
#     for row in data:
#         if row[1] != 'temp':
#             temprature.append(row[1])
# print(temprature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# # print(data)
#
# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data['temp'].to_list()
# print(round(sum(temp_list)/len(temp_list) , 2))


# c = data["temp"].mean()
#
# print(c)

# c = data["temp"].max()
# print(c)

# max_temp = data["temp"].max()

# print(data[data['temp'] == max_temp])


# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9.5 + 32
# print(monday_temp_F)
# import pandas as pd
# data = pd.read_csv(sq.csv)
#
# print(data)
#


import tkinter

window = tkinter.Tk()
window.title("Calculator")

window.mainloop()
