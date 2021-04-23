# exam 2.9 page 53
import sys
from urllib.request import urlopen
sys.stdout = open('dp.html','w',encoding='utf8')
f=urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
encoding = f.info().get_content_charset(failobj="utf-8")
print('encoding : ',encoding, file=sys.stderr)
text = f.read().decode(encoding)
print(text)
sys.stdout.close()

