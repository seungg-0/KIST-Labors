import pandas as pd
from os import walk
import sys

temp = pd.read_excel('../resources/infection-result/서울.xlsx', nrows=0)
temp_columns = temp.columns
top_column = temp_columns.values.tolist()
where = top_column[0]
categories = top_column[3::4]
# print(where)
# print(*categories, sep=", ")

# df = pd.read_excel('../resources/infection-result/서울.xlsx', header=1)
# df = df.replace(['X', 'O'], [0, 1])
# print(df.head())
# print(df.columns.values)
# df.to_csv("서울.csv")

# print(df)
# print(df.loc[1, :].values)
# print(df.loc[0, :].keys)

path = '../resources/scoring_data/'
filenames = []
for (_, _, filename) in walk(path):
    filenames.extend(filename)

print(*filenames)
df = pd.read_csv(path + filenames[0], encoding='euc-kr')
df['지역'] = filenames[0].split('.')[0]
print(df)
