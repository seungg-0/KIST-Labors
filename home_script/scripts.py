from os import listdir
import pandas as pd
import numpy as np
from my_path import paths

# # os.listdir()
#
# population = pd.read_csv(paths.population + 'my_population.csv', index_col=0, squeeze=True)
# # print(population["대구"])
#
# temp = paths.scoring
# file_list = listdir(temp)
# score_list = []
# for file_name in file_list:
#     df = pd.read_csv(temp + file_name, encoding='euc-kr', usecols=[0, 1])
#     area_name = file_name.split(".")[0]
#     df = df.iloc[:-7, :]
#     score_list.append(df)
#
#
# temp = paths.infection_population
# file_list = listdir(temp)
# df_list = []
# index = 0
# for file_name in file_list:
#     df = pd.read_csv(temp + file_name, encoding='euc-kr')
#     area_name = file_name.split(".")[0]
#     df["지역"] = area_name
#     df = df.rename(columns={"신고일": "확진자수", "data": "날짜"})
#     df["비율"] = df["확진자수"] / population[area_name]
#     df["단계"] = score_list[index]["단계"]
#     df.to_csv(area_name + "_비율.csv", index=False, encoding='euc-kr')
#     df_list.append(df)
#     index += 0
# #
# # full_df = pd.concat(df_list)
# # print(full_df)
# # full_df.to_csv("종합_비율.csv", index=False, encoding='euc-kr')

df = pd.read_csv("group_by.csv", encoding='euc-kr')
stage = 0
df_list = []
new_df = pd.DataFrame(columns=["date", "avg_infect_ratio", "stage", "area"])
for index, row in df.iterrows():
    pre_stage = stage
    stage = row['단계']
    if pre_stage != 0 and pre_stage != stage:
        temp = df.iloc[index - 7: index + 6, :]
        custom_row0 = [df.iloc[index - 1, :]["날짜"], df.iloc[index - 7: index - 1, :]["비율"].mean(), df.iloc[index - 1, :]['단계'],
                       df.iloc[index - 1, :]["지역"]]
        custom_row1 = [df.iloc[index, :]["날짜"], df.iloc[index: index + 6, :]["비율"].mean(), df.iloc[index, :]['단계'],
                       df.iloc[index, :]["지역"]]
        new_df.loc[len(new_df)] = custom_row0
        new_df.loc[len(new_df)] = custom_row1

# print(new_df)
for _, df in new_df.groupby(["area"]):
    print(df)
    df.to_csv(df.iloc[0, :]["area"] + "_avg.csv", index=False, encoding="euc-kr")
new_df.to_csv("avg_7day_areas_date_stage.csv", index=False, encoding="euc-kr")
# very_new_df = pd.concat(df_list)
# very_new_df.to_csv("very_new_df.csv", encoding='euc-kr', index=False)
# print(very_new_df)
# df.to_csv("group_by.csv", index=False, encoding='euc-kr')
# ref = df.drop_duplicates(subset=['단계'])
# print(ref)

# new_df = df.groupby(['지역', '단계']).head(7)
# new_df = new_df.loc[new_df['단계'] > 0.4]
# print(new_df)

# new_df.to_csv("group_by.csv", index=False, encoding='euc-kr')
# test = new_df.groupby(np.arange(len(new_df.index))//7).mean()
# test.to_csv("average.csv", index=False, encoding='euc-kr')
# print(test)
# df.drop_duplicates(subset=['지역', '단계'], inplace=True)
