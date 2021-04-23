import requests
response = requests.get("https://www.weather.go.kr/weather/observation/currentweather.jsp")
# requests 명령어를 수행해 url에 접속하여 데이터 가져오고
# 성공 여부를 리턴함 200 출력
# print(response)
# print("response.content",response.content) # 너무 보기 어렵다
# beautifulsoap를 이용해서
# 조건에 만족하는 것을 찾아주는 것을 parsing 이라한다
# 조건에 만족하는 태그를 찾아줌
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup) # 그래도 복잡하다.
# find("xxx") : 조건이 1개 일 때 사용해서 찾아준다.
# find_all("xxx","yyy") : 조건이 1개 이상일 때 찾는 방법
table = soup.find("table")
print("#"*80)
# print(table)
# table에서 찾는거나 li태그로 찾는 거나 같은 결과 출력 된다.
# li_list = soup.find_all("li",{"class":"div-9"})
# print("li 태그에 class가 div-9인 것들과 그 안에 포함된 것들 까지",li_list)

# table 태그 안에서 tr태그 속 필요한 기상정보만 빼오기
tr_list = list(table.find_all("tr")) # table 태그 안에서 tr태그 속 필요한 기상정보만 빼오기
                                     # 이니멀레이트 값이라 데이터가 저장되지않고 사라진다. list 타입으로 받아야 한다

# print(tr_list)
# print("*"*80)
data = [] # 저장할 리스트 목록
for tr in tr_list:
    # print(tr)
    # print("*" * 80)
    td_list = list(tr.find_all("td")) # tr 안에서 td를 찾는다
                                      # 이니멀레이트 값이라 데이터가 저장되지않고 사라진다. list 타입으로 받아야 한다
    # print(td_list)
    if len(td_list) > 0:
        # print("지역 = ", td_list[0])
        # print("지역 = ", td_list[0].find("a"))
        # print("지역 = ", td_list[0].find("a").text) # .text를 붙이면 태그<td><tr>같은거 없이 내용만 추출됨
        # print("온도 = ", td_list[5].text)
        # print("습도 = ", td_list[10].text)
        for td in td_list:
            if td.find('a'):
                point = td.find('a').text
                temperature = td_list[5].text
                humidity = td_list[10].text
                data.append([point, temperature, humidity])
# 2중 리스트 를 pandas로 어떻게 표현하면 좋을지 생각해볼것
# print(data)
# 엑셀 csv 파일로 만들기
with open('weather.csv','w') as file:
    file.write('point,temperature,humidity\n')
    for i in data:
        file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2]))
        # \n 을 적어주지 않으면 데이터가 입력되지 않는다.
