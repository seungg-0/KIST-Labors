import pandas as pd
from os import walk

# temp = pd.read_excel('../resources/infection-result/서울.xlsx', nrows=0)
# temp_columns = temp.columns
# top_column = temp_columns.values.tolist()
# where = top_column[0]
# categories = top_column[3::4]
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

dfs = []
for name in filenames:
    df = pd.read_csv(path + name, encoding='euc-kr')
    df['지역'] = name.split('.')[0]
    dfs.append(df)
    
full_df = pd.concat(dfs)
full_df = full_df.sort_values(by=['날짜'])

seoul_df = full_df.loc[full_df['지역'] == '서울']
test2 = seoul_df.drop_duplicates(subset=seoul_df.columns.values[1:])
test = seoul_df.iloc[:, 1:]
test2 = test2.sort_values(by=['단계'])
test2.to_csv("drop_duplicate_seoul.csv")

data = full_df.drop_duplicates(subset=full_df.columns.values[2:-1])
data = data.sort_values(by=['단계'])
data.to_csv("unique_policy.csv")
