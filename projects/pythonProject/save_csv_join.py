import sys
import csv

data = [['1', '상하이', '24150000'],['2', '카라치', '23500000'],['3', '베이징', '21516000'],['4', '텐진', '14722100'],['5', '이스탄불', '14160467']]

csvfile = open("top_cities.csv","w",newline="")

csvwriter = csv.writer(csvfile)
for row in data:
    csvwriter.writerow(row)
csvfile.close