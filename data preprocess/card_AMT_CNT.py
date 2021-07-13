# -*- coding: utf-8 -*-
import pandas as pd
import os

city_name = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '울산', '인천', '전남', '전북', '제주', '충남', '충북']
card_business_list = ['음식점', '제과점', '놀이공원', '스포츠시설', '골프장', '유흥', '백화점', '면세점', '쇼핑기타', '아울렛']
day_col_list_CNT = ['CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']
index_list = ['2020-05-03','2020-05-04','2020-05-05','2020-05-06','2020-05-07','2020-05-08','2020-05-09','2020-05-10','2020-05-11','2020-05-12','2020-05-13','2020-05-14','2020-05-15','2020-05-16','2020-05-17','2020-05-18','2020-05-19','2020-05-20','2020-05-21','2020-05-22','2020-05-23','2020-05-24','2020-05-25','2020-05-26','2020-05-27','2020-05-28','2020-05-29','2020-05-30','2020-05-31','2020-06-01','2020-06-02','2020-06-03','2020-06-04','2020-06-05','2020-06-06','2020-06-07','2020-06-08','2020-06-09','2020-06-10','2020-06-11','2020-06-12','2020-06-13','2020-06-14','2020-06-15','2020-06-16','2020-06-17','2020-06-18','2020-06-19','2020-06-20','2020-06-21','2020-06-22','2020-06-23','2020-06-24','2020-06-25','2020-06-26','2020-06-27','2020-06-28','2020-06-29','2020-06-30','2020-07-01','2020-07-02','2020-07-03','2020-07-04','2020-07-05','2020-07-06','2020-07-07','2020-07-08','2020-07-09','2020-07-10','2020-07-11','2020-07-12','2020-07-13','2020-07-14','2020-07-15','2020-07-16','2020-07-17','2020-07-18','2020-07-19','2020-07-20','2020-07-21','2020-07-22','2020-07-23','2020-07-24','2020-07-25','2020-07-26','2020-07-27','2020-07-28','2020-07-29','2020-07-30','2020-07-31','2020-08-01','2020-08-02','2020-08-03','2020-08-04','2020-08-05','2020-08-06','2020-08-07','2020-08-08','2020-08-09','2020-08-10','2020-08-11','2020-08-12','2020-08-13','2020-08-14','2020-08-15','2020-08-16','2020-08-17','2020-08-18','2020-08-19','2020-08-20','2020-08-21','2020-08-22','2020-08-23','2020-08-24','2020-08-25','2020-08-26','2020-08-27','2020-08-28','2020-08-29','2020-08-30','2020-08-31','2020-09-01','2020-09-02','2020-09-03','2020-09-04','2020-09-05','2020-09-06','2020-09-07','2020-09-08','2020-09-09','2020-09-10','2020-09-11','2020-09-12','2020-09-13','2020-09-14','2020-09-15','2020-09-16','2020-09-17','2020-09-18','2020-09-19','2020-09-20','2020-09-21','2020-09-22','2020-09-23','2020-09-24','2020-09-25','2020-09-26','2020-09-27','2020-09-28','2020-09-29','2020-09-30','2020-10-01','2020-10-02','2020-10-03','2020-10-04','2020-10-05','2020-10-06','2020-10-07','2020-10-08','2020-10-09','2020-10-10','2020-10-11','2020-10-12','2020-10-13','2020-10-14','2020-10-15','2020-10-16','2020-10-17','2020-10-18','2020-10-19','2020-10-20','2020-10-21','2020-10-22','2020-10-23','2020-10-24','2020-10-25','2020-10-26','2020-10-27','2020-10-28','2020-10-29','2020-10-30','2020-10-31','2020-11-01','2020-11-02','2020-11-03','2020-11-04','2020-11-05','2020-11-06','2020-11-07','2020-11-08','2020-11-09','2020-11-10','2020-11-11','2020-11-12','2020-11-13','2020-11-14','2020-11-15','2020-11-16','2020-11-17','2020-11-18','2020-11-19','2020-11-20','2020-11-21','2020-11-22','2020-11-23','2020-11-24','2020-11-25','2020-11-26','2020-11-27','2020-11-28','2020-11-29','2020-11-30','2020-12-01','2020-12-02','2020-12-03','2020-12-04','2020-12-05','2020-12-06','2020-12-07','2020-12-08','2020-12-09','2020-12-10','2020-12-11','2020-12-12','2020-12-13','2020-12-14','2020-12-15','2020-12-16','2020-12-17','2020-12-18','2020-12-19','2020-12-20','2020-12-21','2020-12-22','2020-12-23','2020-12-24','2020-12-25','2020-12-26','2020-12-27','2020-12-28','2020-12-29','2020-12-30','2020-12-31','2021-01-01','2021-01-02','2021-01-03','2021-01-04','2021-01-05','2021-01-06','2021-01-07','2021-01-08','2021-01-09','2021-01-10','2021-01-11','2021-01-12','2021-01-13','2021-01-14','2021-01-15','2021-01-16','2021-01-17','2021-01-18','2021-01-19','2021-01-20','2021-01-21','2021-01-22','2021-01-23','2021-01-24','2021-01-25','2021-01-26','2021-01-27','2021-01-28','2021-01-29','2021-01-30']


card_file_dir = "D:/새 폴더/행안부/card.csv"

card = pd.read_csv(card_file_dir, encoding='cp949', engine='python')  # 카드매출 파일 load
card = card[['주차구분', '가맹점지역', '업종명_중분류', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']]
card['주차구분'] = card['주차구분'].str.split(' ', expand=True)[2]  # '주차구분 column' 2020 1주차 20200101 -> 20200101 형태로 변환
card['가맹점지역'] = card['가맹점지역'].str.split('_', expand=True)[0]  # '가맹점지역 column' 경기_가평군_가평읍 -> 경기 형태로 변환
card = card[card.주차구분 >= '20200427']


empty_data_dict = []
for business_name in card_business_list:  # 카드 매출 전처리_업종별 데이터프레임 생성
    globals()[str(business_name)] = card[card.업종명_중분류 == business_name]
    globals()[str(business_name)] = globals()[str(business_name)][['주차구분', '가맹점지역', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']]
    for city in city_name:
        globals()['{}_{}'.format(business_name, city)] = globals()[str(business_name)][globals()[str(business_name)].가맹점지역 == city]
        globals()['{}_{}'.format(business_name, city)] = globals()['{}_{}'.format(business_name, city)][['주차구분', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']]
        globals()['{}_{}'.format(business_name, city)] = globals()['{}_{}'.format(business_name, city)].groupby('주차구분').sum()
        if len((globals()['{}_{}'.format(business_name, city)])) < 40:
            empty_data_dict.append([business_name, city])
            continue
        globals()['{}_{}daily_CNT_list'.format(business_name, city)] = []
        globals()['{}_{}daily_CNT_list_matrix'.format(business_name, city)] = []
        for col_name in day_col_list_CNT:
            globals()['{}_{}daily_CNT_list_matrix'.format(business_name, city)].append(globals()['{}_{}'.format(business_name, city)][col_name].tolist())
        for i in range(0, len(globals()['{}_{}'.format(business_name, city)])):
            for k in range(0, 7):
                globals()['{}_{}daily_CNT_list'.format(business_name, city)].append(globals()['{}_{}daily_CNT_list_matrix'.format(business_name, city)][k][i])
        del globals()['{}_{}daily_CNT_list'.format(business_name, city)][0:6]
        del globals()['{}_{}daily_CNT_list'.format(business_name, city)][-1]

# 업종명에 '/'가 포함될 경우 변수 동적할탕 코드에서 에러 발생. -> '마트/할인점' 업종 별도 처리
마트할인점 = card[card.업종명_중분류 == '마트/할인점']

마트할인점 = 마트할인점[['주차구분', '가맹점지역', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토','CNT_DAY_일']]
for city in city_name:
    globals()['마트할인점_{}'.format(city)] = 마트할인점[마트할인점.가맹점지역 == city]
    globals()['마트할인점_{}'.format(city)] = globals()['마트할인점_{}'.format(city)][['주차구분', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']]
    globals()['마트할인점_{}'.format(city)] = globals()['마트할인점_{}'.format(city)].groupby('주차구분').sum()
    if len((globals()['마트할인점_{}'.format(city)])) < 40:
        empty_data_dict.append(["마트할인점", city])
        continue
    globals()['마트할인점_{}daily_CNT_list'.format(city)] = []
    globals()['마트할인점_{}daily_CNT_list_matrix'.format(city)] = []
    for col_name in day_col_list_CNT:
        globals()['마트할인점_{}daily_CNT_list_matrix'.format(city)].append(globals()['마트할인점_{}'.format(city)][col_name].tolist())
    for i in range(0, len(globals()['마트할인점_{}'.format(city)])):
        for k in range(0, 7):
            globals()['마트할인점_{}daily_CNT_list'.format(city)].append(globals()['마트할인점_{}daily_CNT_list_matrix'.format(city)][k][i])
    del globals()['마트할인점_{}daily_CNT_list'.format(city)][0:6]
    del globals()['마트할인점_{}daily_CNT_list'.format(city)][-1]
    # print(globals()['마트할인점_{}daily_CNT_list'.format(city)])
    # print(city, "마트할인점", len(globals()['마트할인점_{}'.format(city)]))

# 업종명에 '/'가 포함될 경우 변수 동적할탕 코드에서 에러 발생. -> '커피/음료' 업종 별도 처리
커피음료 = card[card.업종명_중분류 == '커피/음료']

커피음료 = 커피음료[['주차구분', '가맹점지역', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']]
for city in city_name:
    globals()['커피음료_{}'.format(city)] = 커피음료[커피음료.가맹점지역 == city]
    globals()['커피음료_{}'.format(city)] = globals()['커피음료_{}'.format(city)][['주차구분', 'CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']]
    globals()['커피음료_{}'.format(city)] = globals()['커피음료_{}'.format(city)].groupby('주차구분').sum()
    if len((globals()['커피음료_{}'.format(city)])) < 40:
        empty_data_dict.append(["커피음료", city])
        continue
    globals()['커피음료_{}daily_CNT_list'.format(city)] = []
    globals()['커피음료_{}daily_CNT_list_matrix'.format(city)] = []
    for col_name in day_col_list_CNT:
        globals()['커피음료_{}daily_CNT_list_matrix'.format(city)].append(globals()['커피음료_{}'.format(city)][col_name].tolist())
    for i in range(0, len(globals()['커피음료_{}'.format(city)])):
        for k in range(0, 7):
            globals()['커피음료_{}daily_CNT_list'.format(city)].append(globals()['커피음료_{}daily_CNT_list_matrix'.format(city)][k][i])
    del globals()['커피음료_{}daily_CNT_list'.format(city)][0:6]
    del globals()['커피음료_{}daily_CNT_list'.format(city)][-1]
    # print(globals()['커피음료_{}daily_CNT_list'.format(city)])
    # print(city, "커피음료", len(globals()['커피음료_{}'.format(city)]))

new_card_business_list = ['커피음료', '마트할인점', '음식점', '제과점', '놀이공원', '스포츠시설', '골프장', '유흥', '백화점', '면세점', '쇼핑기타', '아울렛']
## 리스트 dataframe 변환 (데이터프레임 지역별로 생성)
# 지역별 CNT df 생성
for city in city_name:
    make_df_list = []
    col_name_CNT = []
    for business_name in new_card_business_list:
        if (((business_name == '놀이공원') and (city == '강원')) or ((business_name == '놀이공원') and (city == '경남')) or ((business_name == '놀이공원') and (city == '경북')) or ((business_name == '놀이공원') and (city == '광주')) or ((business_name == '놀이공원') and (city == '대전')) or ((business_name == '놀이공원') and (city == '부산')) or ((business_name == '놀이공원') and (city == '서울')) or ((business_name == '놀이공원') and (city == '울산')) or((business_name == '놀이공원') and (city == '전남')) or((business_name == '놀이공원') and (city == '전북')) or((business_name == '놀이공원') and (city == '충남')) or((business_name == '놀이공원') and (city == '충북')) or((business_name == '유흥') and (city == '부산')) or((business_name == '백화점') and (city == '강원')) or((business_name == '백화점') and (city == '경북')) or((business_name == '백화점') and (city == '인천')) or((business_name == '백화점') and (city == '전남')) or((business_name == '백화점') and (city == '전북')) or ((business_name == '백화점') and (city == '제주')) or ((business_name == '백화점') and (city == '충북')) or ((business_name == '면세점') and (city == '강원')) or((business_name == '면세점') and (city == '경기')) or ((business_name == '면세점') and (city == '경남')) or ((business_name == '면세점') and (city == '경북')) or((business_name == '면세점') and (city == '광주')) or((business_name == '면세점') and ('대구')) or((business_name == '면세점') and ('대전')) or((business_name == '면세점') and ('부산')) or((business_name == '면세점') and ('울산')) or((business_name == '면세점') and ('전남')) or((business_name == '면세점') and ('전북')) or((business_name == '면세점') and ('충남')) or((business_name == '면세점') and ('충북')) or((business_name == '쇼핑기타') and ('강원')) or((business_name == '쇼핑기타') and ('경기')) or((business_name == '쇼핑기타') and ('경남')) or((business_name == '쇼핑기타') and ('경북')) or((business_name == '쇼핑기타') and ('광주')) or((business_name == '쇼핑기타') and ('대구')) or((business_name == '쇼핑기타') and ('대전')) or((business_name == '쇼핑기타') and ('부산')) or((business_name == '쇼핑기타') and ('울산')) or((business_name == '쇼핑기타') and ('인천')) or((business_name == '쇼핑기타') and ('전남')) or((business_name == '쇼핑기타') and ('전북')) or((business_name == '쇼핑기타') and ('제주')) or((business_name == '쇼핑기타') and ('충남')) or((business_name == '쇼핑기타') and ('충북')) or((business_name == '아울렛') and ('강원')) or((business_name == '아울렛') and ('경기')) or((business_name == '아울렛') and ('광주')) or((business_name == '아울렛') and ('대전')) or((business_name == '아울렛') and ('부산')) or((business_name == '아울렛') and ('울산')) or((business_name == '아울렛') and ('전남')) or((business_name == '아울렛') and ('제주'))):
            continue
        else:
            make_df_list.append(globals()['{}_{}daily_CNT_list'.format(business_name, city)])
            col_name_CNT.append(business_name + 'CNT')
    globals()['{}_df_CNT'.format(city)] = pd.DataFrame(make_df_list, col_name_CNT)


# col_name = ['colname1', 'colname2']
# list1 = [[1, 2, 3], [4, 5, 6]]
# list_df = pd.DataFrame(list1, columns=col_name)
######################################################################### ~ CNT

card = pd.read_csv(card_file_dir, encoding='cp949', engine='python')  # 카드매출 파일 load
card = card[['주차구분', '가맹점지역', '업종명_중분류', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
card['주차구분'] = card['주차구분'].str.split(' ', expand=True)[2]  # '주차구분 column' 2020 1주차 20200101 -> 20200101 형태로 변환
card['가맹점지역'] = card['가맹점지역'].str.split('_', expand=True)[0]  # '가맹점지역 column' 경기_가평군_가평읍 -> 경기 형태로 변환
card = card[card.주차구분 >= '20200427']

day_col_list_AMT = ['AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']

empty_data_dict = []
for business_name in card_business_list:  # 카드 매출 전처리_업종별 데이터프레임 생성
    globals()[str(business_name)] = card[card.업종명_중분류 == business_name]
    globals()[str(business_name)] = globals()[str(business_name)][['주차구분', '가맹점지역', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
    for city in city_name:
        globals()['{}_{}'.format(business_name, city)] = globals()[str(business_name)][globals()[str(business_name)].가맹점지역 == city]
        globals()['{}_{}'.format(business_name, city)] = globals()['{}_{}'.format(business_name, city)][['주차구분', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
        globals()['{}_{}'.format(business_name, city)] = globals()['{}_{}'.format(business_name, city)].groupby('주차구분').sum()
        if len((globals()['{}_{}'.format(business_name, city)])) < 40:
            empty_data_dict.append([business_name, city])
            continue
        globals()['{}_{}daily_AMT_list'.format(business_name, city)] = []
        globals()['{}_{}daily_AMT_list_matrix'.format(business_name, city)] = []
        for col_name in day_col_list_AMT:
            globals()['{}_{}daily_AMT_list_matrix'.format(business_name, city)].append(globals()['{}_{}'.format(business_name, city)][col_name].tolist())
        for i in range(0, len(globals()['{}_{}'.format(business_name, city)])):
            for k in range(0, 7):
                globals()['{}_{}daily_AMT_list'.format(business_name, city)].append(globals()['{}_{}daily_AMT_list_matrix'.format(business_name, city)][k][i])
        del globals()['{}_{}daily_AMT_list'.format(business_name, city)][0:6]
        del globals()['{}_{}daily_AMT_list'.format(business_name, city)][-1]

# 업종명에 '/'가 포함될 경우 변수 동적할탕 코드에서 에러 발생. -> '마트/할인점' 업종 별도 처리
마트할인점 = card[card.업종명_중분류 == '마트/할인점']

마트할인점 = 마트할인점[['주차구분', '가맹점지역', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
for city in city_name:
    globals()['마트할인점_{}'.format(city)] = 마트할인점[마트할인점.가맹점지역 == city]
    globals()['마트할인점_{}'.format(city)] = globals()['마트할인점_{}'.format(city)][['주차구분', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
    globals()['마트할인점_{}'.format(city)] = globals()['마트할인점_{}'.format(city)].groupby('주차구분').sum()
    if len((globals()['마트할인점_{}'.format(city)])) < 40:
        empty_data_dict.append(["마트할인점", city])
        continue
    globals()['마트할인점_{}daily_AMT_list'.format(city)] = []
    globals()['마트할인점_{}daily_AMT_list_matrix'.format(city)] = []
    for col_name in day_col_list_AMT:
        globals()['마트할인점_{}daily_AMT_list_matrix'.format(city)].append(globals()['마트할인점_{}'.format(city)][col_name].tolist())
    for i in range(0, len(globals()['마트할인점_{}'.format(city)])):
        for k in range(0, 7):
            globals()['마트할인점_{}daily_AMT_list'.format(city)].append(globals()['마트할인점_{}daily_AMT_list_matrix'.format(city)][k][i])
    del globals()['마트할인점_{}daily_AMT_list'.format(city)][0:6]
    del globals()['마트할인점_{}daily_AMT_list'.format(city)][-1]


# 업종명에 '/'가 포함될 경우 변수 동적할탕 코드에서 에러 발생. -> '커피/음료' 업종 별도 처리
커피음료 = card[card.업종명_중분류 == '커피/음료']

커피음료 = 커피음료[['주차구분', '가맹점지역', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
for city in city_name:
    globals()['커피음료_{}'.format(city)] = 커피음료[커피음료.가맹점지역 == city]
    globals()['커피음료_{}'.format(city)] = globals()['커피음료_{}'.format(city)][['주차구분', 'AMT_DAY_월', 'AMT_DAY_화', 'AMT_DAY_수', 'AMT_DAY_목', 'AMT_DAY_금', 'AMT_DAY_토', 'AMT_DAY_일']]
    globals()['커피음료_{}'.format(city)] = globals()['커피음료_{}'.format(city)].groupby('주차구분').sum()
    if len((globals()['커피음료_{}'.format(city)])) < 40:
        empty_data_dict.append(["커피음료", city])
        continue
    globals()['커피음료_{}daily_AMT_list'.format(city)] = []
    globals()['커피음료_{}daily_AMT_list_matrix'.format(city)] = []
    for col_name in day_col_list_AMT:
        globals()['커피음료_{}daily_AMT_list_matrix'.format(city)].append(globals()['커피음료_{}'.format(city)][col_name].tolist())
    for i in range(0, len(globals()['커피음료_{}'.format(city)])):
        for k in range(0, 7):
            globals()['커피음료_{}daily_AMT_list'.format(city)].append(globals()['커피음료_{}daily_AMT_list_matrix'.format(city)][k][i])
    del globals()['커피음료_{}daily_AMT_list'.format(city)][0:6]
    del globals()['커피음료_{}daily_AMT_list'.format(city)][-1]

## 리스트 dataframe 변환 (데이터프레임 지역별로 생성)
# 지역별 CNT df 생성
for city in city_name:
    make_df_list = []
    col_name_AMT = []
    for business_name in new_card_business_list:
        if (((business_name == '놀이공원') and (city == '강원')) or ((business_name == '놀이공원') and (city == '경남')) or ((business_name == '놀이공원') and (city == '경북')) or ((business_name == '놀이공원') and (city == '광주')) or ((business_name == '놀이공원') and (city == '대전')) or ((business_name == '놀이공원') and (city == '부산')) or ((business_name == '놀이공원') and (city == '서울')) or ((business_name == '놀이공원') and (city == '울산')) or((business_name == '놀이공원') and (city == '전남')) or((business_name == '놀이공원') and (city == '전북')) or((business_name == '놀이공원') and (city == '충남')) or((business_name == '놀이공원') and (city == '충북')) or((business_name == '유흥') and (city == '부산')) or((business_name == '백화점') and (city == '강원')) or((business_name == '백화점') and (city == '경북')) or((business_name == '백화점') and (city == '인천')) or((business_name == '백화점') and (city == '전남')) or((business_name == '백화점') and (city == '전북')) or ((business_name == '백화점') and (city == '제주')) or ((business_name == '백화점') and (city == '충북')) or ((business_name == '면세점') and (city == '강원')) or((business_name == '면세점') and (city == '경기')) or ((business_name == '면세점') and (city == '경남')) or ((business_name == '면세점') and (city == '경북')) or((business_name == '면세점') and (city == '광주')) or((business_name == '면세점') and ('대구')) or((business_name == '면세점') and ('대전')) or((business_name == '면세점') and ('부산')) or((business_name == '면세점') and ('울산')) or((business_name == '면세점') and ('전남')) or((business_name == '면세점') and ('전북')) or((business_name == '면세점') and ('충남')) or((business_name == '면세점') and ('충북')) or((business_name == '쇼핑기타') and ('강원')) or((business_name == '쇼핑기타') and ('경기')) or((business_name == '쇼핑기타') and ('경남')) or((business_name == '쇼핑기타') and ('경북')) or((business_name == '쇼핑기타') and ('광주')) or((business_name == '쇼핑기타') and ('대구')) or((business_name == '쇼핑기타') and ('대전')) or((business_name == '쇼핑기타') and ('부산')) or((business_name == '쇼핑기타') and ('울산')) or((business_name == '쇼핑기타') and ('인천')) or((business_name == '쇼핑기타') and ('전남')) or((business_name == '쇼핑기타') and ('전북')) or((business_name == '쇼핑기타') and ('제주')) or((business_name == '쇼핑기타') and ('충남')) or((business_name == '쇼핑기타') and ('충북')) or((business_name == '아울렛') and ('강원')) or((business_name == '아울렛') and ('경기')) or((business_name == '아울렛') and ('광주')) or((business_name == '아울렛') and ('대전')) or((business_name == '아울렛') and ('부산')) or((business_name == '아울렛') and ('울산')) or((business_name == '아울렛') and ('전남')) or((business_name == '아울렛') and ('제주'))):
            continue
        else:
            make_df_list.append(globals()['{}_{}daily_AMT_list'.format(business_name, city)])
            col_name_AMT.append(business_name + 'AMT')
    globals()['{}_df_AMT'.format(city)] = pd.DataFrame(make_df_list, col_name_AMT)


for city in city_name:
    result_dir = "card_data_amt_cnt" # 폴더 없으면 생성해서 파일 저장
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    result = pd.concat([globals()['{}_df_CNT'.format(city)],globals()['{}_df_AMT'.format(city)]], axis = 0)
    result = result.transpose()
    result.index = index_list
    file_dir = os.path.join(city + ".csv")
    result.to_csv(file_dir, encoding='UTF-8')
