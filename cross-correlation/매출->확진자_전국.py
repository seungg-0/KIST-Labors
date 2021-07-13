import pandas as pd
import numpy as np
import os

# 변수 동적할당을 위한 list
city_name = ['강원', '경기', '경남', '경북', '광주', '대구', '대전', '부산', '서울', '울산', '인천', '전남', '전북', '제주', '충남', '충북']
card_business_list = ['음식점', '제과점', '놀이공원', '스포츠시설', '골프장', '유흥', '백화점', '면세점', '쇼핑기타', '아울렛']
day_col_list = ['CNT_DAY_월', 'CNT_DAY_화', 'CNT_DAY_수', 'CNT_DAY_목', 'CNT_DAY_금', 'CNT_DAY_토', 'CNT_DAY_일']
index_list = [-272, -271,-270,-269,-268,-267,-266,-265,-264,-263,-262,-261,-260,-259,-258,-257,-256,-255,-254,-253,-252,-251,-250,-249,-248,-247,-246,-245,-244,-243,-242,-241,-240,-239,-238,-237,-236,-235,-234,-233,-232,-231,-230,-229,-228,-227,-226,-225,-224,-223,-222,-221,-220,-219,-218,-217,-216,-215,-214,-213,-212,-211,-210,-209,-208,-207,-206,-205,-204,-203,-202,-201,-200,-199,-198,-197,-196,-195,-194,-193,-192,-191,-190,-189,-188,-187,-186,-185,-184,-183,-182,-181,-180,-179,-178,-177,-176,-175,-174,-173,-172,-171,-170,-169,-168,-167,-166,-165,-164,-163,-162,-161,-160,-159,-158,-157,-156,-155,-154,-153,-152,-151,-150,-149,-148,-147,-146,-145,-144,-143,-142,-141,-140,-139,-138,-137,-136,-135,-134,-133,-132,-131,-130,-129,-128,-127,-126,-125,-124,-123,-122,-121,-120,-119,-118,-117,-116,-115,-114,-113,-112,-111,-110,-109,-108,-107,-106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80,-79,-78,-77,-76,-75,-74,-73,-72,-71,-70,-69,-68,-67,-66,-65,-64,-63,-62,-61,-60,-59,-58,-57,-56,-55,-54,-53,-52,-51,-50,-49,-48,-47,-46,-45,-44,-43,-42,-41,-40,-39,-38,-37,-36,-35,-34,-33,-32,-31,-30,-29,-28,-27,-26,-25,-24,-23,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271, 272]


# 파일 경로
card_file_dir = "D:/새 폴더/행안부/card.csv"

for city in city_name:
    infected_file_name = "D:/새 폴더/행안부/infected/" + city + ".csv"
    globals()['y{}'.format(city)] = pd.read_csv(infected_file_name, encoding='cp949') # y값 csv파일 불러오기
    globals()['y{}'.format(city)] = globals()['y{}'.format(city)][['신고일']] # 필요한 칼럼 추출
    globals()['y{}'.format(city)] = globals()['y{}'.format(city)].rename(columns={'신고일': '확진자수'})


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
        for col_name in day_col_list:
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
    for col_name in day_col_list:
        globals()['마트할인점_{}daily_CNT_list_matrix'.format(city)].append(globals()['마트할인점_{}'.format(city)][col_name].tolist())
    for i in range(0, len(globals()['마트할인점_{}'.format(city)])):
        for k in range(0, 7):
            globals()['마트할인점_{}daily_CNT_list'.format(city)].append(globals()['마트할인점_{}daily_CNT_list_matrix'.format(city)][k][i])
    del globals()['마트할인점_{}daily_CNT_list'.format(city)][0:6]
    del globals()['마트할인점_{}daily_CNT_list'.format(city)][-1]

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
    for col_name in day_col_list:
        globals()['커피음료_{}daily_CNT_list_matrix'.format(city)].append(globals()['커피음료_{}'.format(city)][col_name].tolist())
    for i in range(0, len(globals()['커피음료_{}'.format(city)])):
        for k in range(0, 7):
            globals()['커피음료_{}daily_CNT_list'.format(city)].append(globals()['커피음료_{}daily_CNT_list_matrix'.format(city)][k][i])
    del globals()['커피음료_{}daily_CNT_list'.format(city)][0:6]
    del globals()['커피음료_{}daily_CNT_list'.format(city)][-1]

# '/'포함되어 별도 처리 해주었던 두 업좀(커피음료, 마트할인점)을 xcorr진행시에는 다른 업종들과 함께 한 번에 처리해주기 위한 리스트
new_card_business_list = ['커피음료', '마트할인점', '음식점', '제과점', '놀이공원', '스포츠시설', '골프장', '유흥', '백화점', '면세점', '쇼핑기타', '아울렛']
for business_name in new_card_business_list:
    result_dir = business_name + "_xcorr_result_CNT/" # 폴더 없으면 생성해서 파일 저장
    if not os.path.isdir(result_dir):
        os.mkdir(result_dir)
    for city in city_name:
        if (((business_name == '놀이공원') and (city == '강원')) or ((business_name == '놀이공원') and (city == '경남')) or ((business_name == '놀이공원') and (city == '경북')) or ((business_name == '놀이공원') and (city == '광주')) or ((business_name == '놀이공원') and (city == '대전')) or ((business_name == '놀이공원') and (city == '부산')) or ((business_name == '놀이공원') and (city == '서울')) or ((business_name == '놀이공원') and (city == '울산')) or((business_name == '놀이공원') and (city == '전남')) or((business_name == '놀이공원') and (city == '전북')) or((business_name == '놀이공원') and (city == '충남')) or((business_name == '놀이공원') and (city == '충북')) or((business_name == '유흥') and (city == '부산')) or((business_name == '백화점') and (city == '강원')) or((business_name == '백화점') and (city == '경북')) or((business_name == '백화점') and (city == '인천')) or((business_name == '백화점') and (city == '전남')) or((business_name == '백화점') and (city == '전북')) or ((business_name == '백화점') and (city == '제주')) or ((business_name == '백화점') and (city == '충북')) or ((business_name == '면세점') and (city == '강원')) or((business_name == '면세점') and (city == '경기')) or ((business_name == '면세점') and (city == '경남')) or ((business_name == '면세점') and (city == '경북')) or((business_name == '면세점') and (city == '광주')) or((business_name == '면세점') and ('대구')) or((business_name == '면세점') and ('대전')) or((business_name == '면세점') and ('부산')) or((business_name == '면세점') and ('울산')) or((business_name == '면세점') and ('전남')) or((business_name == '면세점') and ('전북')) or((business_name == '면세점') and ('충남')) or((business_name == '면세점') and ('충북')) or((business_name == '쇼핑기타') and ('강원')) or((business_name == '쇼핑기타') and ('경기')) or((business_name == '쇼핑기타') and ('경남')) or((business_name == '쇼핑기타') and ('경북')) or((business_name == '쇼핑기타') and ('광주')) or((business_name == '쇼핑기타') and ('대구')) or((business_name == '쇼핑기타') and ('대전')) or((business_name == '쇼핑기타') and ('부산')) or((business_name == '쇼핑기타') and ('울산')) or((business_name == '쇼핑기타') and ('인천')) or((business_name == '쇼핑기타') and ('전남')) or((business_name == '쇼핑기타') and ('전북')) or((business_name == '쇼핑기타') and ('제주')) or((business_name == '쇼핑기타') and ('충남')) or((business_name == '쇼핑기타') and ('충북')) or((business_name == '아울렛') and ('강원')) or((business_name == '아울렛') and ('경기')) or((business_name == '아울렛') and ('광주')) or((business_name == '아울렛') and ('대전')) or((business_name == '아울렛') and ('부산')) or((business_name == '아울렛') and ('울산')) or((business_name == '아울렛') and ('전남')) or((business_name == '아울렛') and ('제주'))):
            continue
        else:
            x = globals()['{}_{}daily_CNT_list'.format(business_name, city)]
            y = globals()['y{}'.format(city)]['확진자수'].tolist() # '확진자수'칼럼 리스트 변환
            y = y[0:273]
            y = np.array(y)
            x = np.array(x)
            x = (x - np.mean(x)) / (np.std(x) * len(x))
            y = (y - np.mean(y)) / (np.std(y))
            result = np.correlate(x, y, mode='full')
            column_names = ["corr"]
            result = pd.DataFrame(result, columns=column_names)
            result.index = index_list
            file_dir = os.path.join(business_name + "_xcorr_result_CNT/", city + ".csv")
            result.to_csv(file_dir, encoding='UTF-8')
