# import sys
# from urllib.request import urlopen
# sys.stdout = open('rss.xml','w')
# f=urlopen('http://www.kma.go.kr/wether/foreceast/mid-term-rss3.jsp?stnId=109')
# encoding = f.info().get_content_charset(failobj="utf-8")
# print('encoding : ',encoding, file=sys.stderr)
# text = f.read().decode(encoding)
# print(text)
# sys.stdout.close() 안된다 망했다
