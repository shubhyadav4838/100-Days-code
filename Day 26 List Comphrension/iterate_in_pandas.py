import pandas as pd

student_dict = {
    "student":["John", "Mary", "Peter"],
    "score":[70, 80, 90]
}

student_dataframe = pd.DataFrame(student_dict)
# for (key, value) in student_dataframe.items():
#     print(key)
#     print(value)

for (index, row) in student_dataframe.iterrows():
    print(row.score)