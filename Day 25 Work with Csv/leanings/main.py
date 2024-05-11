import pandas

# data = pandas.read_csv("100 Days code\Day 25 Work with Csv\weather_data.csv")
# data_to_dict = data.to_dict()
# # print(data_to_dict)
# temp_list = data["temp"].to_list()

# # Print the data with the maximum temperature
# # print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)

# Create the dataframe from scratch
# data_dict = {
#     "students":["Amy", "James", "Lily"],
#     "scores":[50, 80, 100],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# Working with the squirrel dataset
data = pandas.read_csv("100 Days code/Day 25 Work with Csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240511.csv")

gray_squirrels_count = len(data[data['Primary Fur Color']=='Gray'])
red_squirrels_count = len(data[data['Primary Fur Color']=='Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color']=='Black'])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_squirrels_count, red_squirrels_count, black_squirrels_count]
    
} 
squirrel_data = pandas.DataFrame(data_dict)
squirrel_data.to_csv("squirrel_counts.csv")