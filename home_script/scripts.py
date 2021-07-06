from os import listdir
import pandas as pd
from my_path import paths

# os.listdir()

population = pd.read_csv(paths.population + 'my_population.csv', index_col=0, squeeze=True)
# print(population["대구"])

temp = paths.scoring
file_list = listdir(temp)
score_list = []
for file_name in file_list:
    df = pd.read_csv(temp + file_name, encoding='euc-kr', usecols=[0, 1])
    area_name = file_name.split(".")[0]
    df = df.iloc[:-7, :]
    score_list.append(df)


temp = paths.infection_population
file_list = listdir(temp)
df_list = []
index = 0
for file_name in file_list:
    df = pd.read_csv(temp + file_name, encoding='euc-kr')
    area_name = file_name.split(".")[0]
    df["지역"] = area_name
    df = df.rename(columns={"신고일": "확진자수", "data": "날짜"})
    df["비율"] = df["확진자수"] / population[area_name]
    df["단계"] = score_list[index]["단계"]
    df.to_csv(area_name + "_비율.csv", index=False, encoding='euc-kr')
    df_list.append(df)
    index += 0

full_df = pd.concat(df_list)
print(full_df)
full_df.to_csv("종합_비율.csv", index=False, encoding='euc-kr')


