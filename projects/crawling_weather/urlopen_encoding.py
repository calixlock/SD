#page 53 ex 2.9
import sys
from urllib.request import urlopen
f=urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
encoding = f.info().get_content_charset(failobj="utf-8")
print('encoding : ',encoding, file=sys.stderr)
text = f.read().decode(encoding)
print(text)
