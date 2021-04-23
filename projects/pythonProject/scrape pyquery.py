# pip install pyquery 깔렸는지 확인
from pyquery import PyQuery as pq
d = pq(url = 'https://www.hanbit.co.kr/store/books/full_book_list.html')

# a = d('a').text()
a = d.attr["class"]
print(a)