from lxml import etree
import urllib.request as ur
from bs4 import BeautifulSoup

xml = 'http://apis.data.go.kr/6410000/buslocationservice/getBusLocationList?serviceKey=5qz%2FJhVhdN6Bn8Jc4bGkrQANIoI1zu7EAUE8YbKX5jqJ8kK%2Ba1An2kFEn%2Fx7u34ZzhZgBQ0qSzG09GNshyizKg%3D%3D&routeId=233000031'

xml = ur.urlopen(xml)
soup = BeautifulSoup(xml, 'lxml')
# print(soup)
data = soup.find_all('buslocationlist')
file_data = []
for line in data:
    if line.find('plateno'):
        plateno = line.find('plateno').text
        platetype = line.find('platetype').text
        remainseat = line.find('remainseatcnt').text
        routeid = line.find('routeid').text
        stationid = line.find('stationid').text
    # print("{}\t{}\t{}\t{}\t{}".format(차량번호, 차종, 차량_빈자리, 노선_아이디, 정류소_아이디))
    file_data.append([plateno, platetype, remainseat, routeid, stationid])
# 데이터 2중 리스트에 들어 있는지 확인
# print(file_data)

# csv 파일 저장
with open('bus_file.csv', 'w', encoding='utf-8') as file:
    file.write('차량번호,차종,차량_빈자리,노선_아이디,정류소_아이디\n')
    for i in file_data:
        file.write('{0},{1},{2},{3},{4}\n'.format(i[0], i[1], i[2], i[3], i[4]))