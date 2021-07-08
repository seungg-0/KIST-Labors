from os import listdir
import pandas as pd
import numpy as np
from my_path import paths

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
#     index += 1
#
# full_df = pd.concat(df_list)
# print(full_df)
# full_df.to_csv("종합_비율.csv", index=False, encoding='euc-kr')




df = pd.read_csv("종합_비율.csv", encoding='euc-kr')
stage = 0
df_list = []
new_df = pd.DataFrame(columns=["날짜", "해당조정단계_감염자비율", "조정단계", "지역"])
for index, row in df.iterrows():
    pre_stage = stage
    stage = row['단계']
    if pre_stage != 0 and pre_stage != stage and df.iloc[index, :]["날짜"] != '2020-05-03':
        # print(df.iloc[index - 1, :]["날짜"], df.iloc[index, :]["날짜"])
        # print(pre_stage, stage)
        custom_row0 = [df.iloc[index - 1, :]["날짜"], df.iloc[index - 7: index - 1, :]["비율"].mean(), df.iloc[index - 1, :]['단계'],
                       df.iloc[index - 1, :]["지역"]]
        custom_row1 = [df.iloc[index, :]["날짜"], df.iloc[index: index + 6, :]["비율"].mean(), df.iloc[index, :]['단계'],
                       df.iloc[index, :]["지역"]]
        new_df.loc[len(new_df)] = custom_row0
        new_df.loc[len(new_df)] = custom_row1

for _, df in new_df.groupby(["지역"]):
    # print(df)
    df.to_csv(df.iloc[0, :]["지역"] + "_avg.csv", index=False, encoding="euc-kr")
new_df.to_csv("avg_7day_areas_date_stage.csv", index=False, encoding="euc-kr")
new_df.to_csv("avg_7day_areas_date_stage_utf-8.csv", index=False, encoding='utf-8')



df = pd.read_csv('avg_7day_areas_date_stage.csv', encoding='euc-kr')
means = df['해당조정단계_감염자비율'].groupby(df.index // 2).mean()
even = df.iloc[::2].copy() # even
odd = df.iloc[1::2].copy() # odd
odd['means'] = means.tolist()
odd.drop(columns=['해당조정단계_감염자비율'], inplace=True)
odd.rename(columns={"means": '해당조정단계_감염자비율'}, inplace=True)
print(odd)
data = odd.groupby(['조정단계', '지역']).mean()
data.to_csv("fixed_avg_stage_areas.csv", encoding='euc-kr')
