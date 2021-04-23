import pandas as pd
import numpy as np
import requests  # url 접속 : 코로나 환자 정보 가져올 패키지

# 서울시 코로나 데이터의 1페이지의 100개의 데이터를 수집하는 url을 변수에 저장
url = f"https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw=1&start=0&length=100"
print("url = ", url )
# requests.get(url) : url에 접속해서 서울시 코로나 데이터 1페이지의 데이터를 수집하고 성공 실패 여부를 리턴
# response : 수집의 성공여부가 저장 성공했으면 200이 저장되 있음
response = requests.get(url)
print("response = ", response)

# response.json() : 수집된 데이터를 JSON (Dictionary) 형태로 리턴
# data_json : 수집된 정보를 저장한 변수
data_json = response.json()
# 수집된 데이터를 출력
print("data_json = ", data_json)

# data_json 에 저장된 수집정보는 다음과 같다
# data_json =  {'draw': 1, 'recordsTotal': 14071, 'recordsFiltered': 14071 ...}
# data_json 의 타입은 dictionary 로 전체 데이터의 개수는 record_Total 키에 저장되 있음
# 전체 데이터수를 조회해서 변수 records_total에 대입
records_total = data_json['recordsTotal']
print("records_total=",records_total)

# 코로나 확진자 정보는 1페이지당 100명씩 저장되 있음
# 코로나 확진자 정보의 마지막 페이지를 계산해서 end_page 에 대입

# (records_total % 100) == 0 : 전체 데이터수 (전체 확진자수) 를 100 으로 나눈 나머지가 0 일때 (
#                               전체 확진자 수가 100 의 배수
if (records_total % 100) == 0:
    # (records_total // 100) : record_total (전체 확진자수) 를 100 으로 나눈 몫 이 페이지 수
    # 예를 들어서 record_total 이 100의 배수인 1400 이라고 하면 1400 을 100으로 나눈 몫 14가 페이지 수
    end_page = (records_total // 100)
else:
    # record_total (전체 확진자 수) 가 100 의 배수가 아닐때
    # 예를 들어서 record_total이 100 의 배수가 아닌 1401 이라고 하면 1401 을 100으로 나눈 몫 14 에 1을 더한 15가 페이지수
    end_page = (records_total // 100) + 1

print("end_page = ", end_page)


""" 전체 데이터 수집 함수"""
def get_seoul_covid19(page_no):
    print("get_seoul_covid19 함수 호출")
    # 1페이지 -> 시작 번호 0
    # 2페이지 -> 시작 번호 100
    # 3 페이지 -> 시작번호 200
    # 시작 번호 -> (페이지-1)*100
    start_no = (page_no - 1) * 100

    url = f"https://news.seoul.go.kr/api/27/getCorona19Status/get_status_ajax.php?draw={page_no}&start={start_no}&length=100"

    # print("url = ", url)

    response = requests.get(url)  # url 접속해서 코로나 확진자 정보 가져옴
    # print("response = ", response)
    # 잘가져오면 성공 200 리턴
    # url      실패 이 틀림 404 리턴
    # 서버에러  실패 500 or 505 리턴

    data_json = response.json()  # 수집된 정보를 저장한 변수
    # print("data_json = ", data_json)  # dictionary 형태

    records_total = data_json['recordsTotal']

    # print("record_Total = ", record_total)

    return data_json

# 1page의 코로나 확진자 정보 수집하여 데이터 파악
get_seoul_covid19(1)

# print("end_page = ", end_page)

# data = data_json["data"]

# print("data = ", data)

# 전체 데이터 가져오기
import time
from tqdm import trange

patient_list = []

#for page_no in trange(1, end_page + 1): # 전체 페이지 데이터
for page_no in trange(30, 33): # 개발과정에서 실험용으로  page를 몇 개 지정(end page까지 너무 오래걸림)
    # print("page_no = ", page_no)
    one_page = get_seoul_covid19(page_no)
    # print("one_page = ", one_page)
    # patient = one_page["data"]
    # print("patient = ", patient)  # 결과값이 너무길어 표로 만들고 싶다.

    patient = pd.DataFrame(one_page["data"]) # pandas를 이용해 표로 만들음
    # print("patient = ", patient)
    # print("=" * 80)
    patient_list.append(patient)
    # time.sleep(0.1) # 시간 지연

# print("반복문 종료 후\n", patient_list)
# pandas 패키지를 이용하여 concat하여 하나의 데이터 프레임으로 구성
df_all = pd.concat(patient_list)
print("*"* 80)
# 데이터 프레임의 컬럼명을 정해준다.
df_all.columns = ["발생번호", "환자번호", "확진일", "거주지", "여행력", "접촉력", "퇴원현황" ]
print(df_all)

# print("칸이름 설정후 df_all ")
# print("@"* 80)
# print(df_all)
# print("발생번호 칸 출력")
# print(df_all["발생번호"])

import re

def extract_number(num_string):

   if type(num_string) == str:
    # print("extract_number 호출")
    # print("num_string = ", num_string)
    num_string=num_string.replace("corona19","")
    #
    num =re.sub("[^0-9]","",num_string)
    # 인터넷에서 수집한 데이터는 모두 문자 데이터이다.
    num = int(num)
    # print("특정 문자 제거 후\t", num)

    return num

# print("#"*80)
# # apply 대신 map을 사용해도 문제없다.
# df_all["발생번호"]=df_all["발생번호"].apply(extract_number)
#
# print(df_all["발생번호"])
def extract_text(text):
    print(text)

df_all["퇴원현황"]=df_all["퇴원현황"].map(extract_text)

print(df_all["퇴원현황"])
print(df_all)