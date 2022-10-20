import pandas
#Trying to pull a request 
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")


# data_temp = data["temp"].to_list()
# print(data_temp)
# for temp in data_temp:
#     total = total + temp
# list_size = len(data_temp)
# avg = round(total/list_size, 2)
# #print(f"The average temperature is {avg}")
# maximum = data["temp"].max()
# #print(data[data.temp == maximum])
      #Creating a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
