import csv
from lxml import etree
import urllib.request as ur
from bs4 import BeautifulSoup as bs

page = ur.urlopen(
    'http://apis.data.go.kr/B551015/API187/HorseRaceInfo?ServiceKey=76n2%2FBMj9qHKd8NmTfLTNcjpf7z2b2c0Tffy2TZ%2FqVctfORcjQCQmORviN83yV20U%2BevuafyWs1DT0aIlqD8Zw%3D%3D&numOfRows=10&pageNo=1&ym_fr=201901&ym_to=202012')
soup = bs(page, 'lxml')
items = soup.findAll('item')

# 파일을 엽니다. newline=''으로 줄바꿈 코드의 자동 변환을 제어합니다.
with open('item.csv', 'w', newline='', encoding='utf-8') as f:
    # csv.writer는 파일 객체를 매개변수로 지정합니다.
    writer = csv.writer(f)
    # 첫 번째 줄에는 헤더를 작성합니다.
    writer.writerow(['met', 'rank', 'rckrflag', 'rckrflagtext', 'rccnt', 'yyyymm'])
    # writerows()에 리스트를 전달하면 여러 개의 값을 출력합니다.
    for item in items:
        writer.writerows([item.meet.text])
# [item.meet.text, item.rank.text, item.rckrflag.text, item.rckrflagtext.text, item.rccnt.text, item.yyyymm.text]

#작업중!!!!!!!!!!!!1




