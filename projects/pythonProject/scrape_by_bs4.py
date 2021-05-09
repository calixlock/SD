import requests
from bs4 import BeautifulSoup
# 방법 1
# webpage = requests.get("https://www.hanbit.co.kr/store/books/full_book_list.html")
# # print(webpage.text)
# soup = BeautifulSoup(webpage.content, "html.parser")
# # print(soup)
# for a in soup.find_all('a'):
#     print(a.get('href'), a.text)

# # 방법 2 // 문제발생
#
# with open('full_book_list.html') as f:
#     soup = BeautifulSoup(f, "html.parser")
#
# for a in soup.find_all('a'):
#     print(a.get('href'), a.text)