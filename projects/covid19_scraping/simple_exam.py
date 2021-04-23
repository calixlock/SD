# name = "홍길동"
# today = "2021/01/12"
# str1 = "안녕 {name} 오늘은 {today} 이네"
# print("str1 = " , str1)
#
# str2 = f"안녕 {name} 오늘은 {today} 이네"
# print("str2 = " , str2)
#

# for page_no in range(10):
#     print("page_no = ", page_no)
#     url = f"http://www.aa.com?draw={page_no}"
#     print("url = ", url)
#     print("*" * 50)
#
# import time
# for i in range(10):
#     print("*" * i)
#     print("i = ", i)
#     time.sleep(0.1)


# import pandas
# lst = [["길동",90,100], ["길순", 99 ,80], ["몽룡", 98, 100]]
# print("lst = ", lst)
# print("pandas.DataFrame(lst) = ", pandas.DataFrame(lst))
#
#
#
# list1=[]
# for i in range(10):
#     name = input("너의 이름 ?")
#     list1.append(name)
#     print("name = ", name)
# print(list1)


import re # 특정 규칙에 맞는 문자 찾아서 다른 글자로 변환 패키지
          # 한글을 찾아서 "&" 변환
          # 영어를 찾아서 "*" 변환
          # 숫자를 찾아서 "!" 변환
문자열이저장된변수 = "안녕하세요 Hello 123123"
# re.sub  >> 규칙을 사용
# [가~힣]까지의 한글을 찾아서 "&" 변환
# 한글바꾸기 = re.sub("[가-힣]", "%", 문자열이저장된변수) # 규칙[가-힣]에 일치하는 글자 찾아서 바꿀글자[^^]로 문자열이 저장된 변수 수정
# print("한글 변환 = ",한글바꾸기)
# 숫자바꾸기 = re.sub("[0-9]", "!", 문자열이저장된변수) # 규칙[가-힣]에 일치하는 글자 찾아서 바꿀글자[^^]로 문자열이 저장된 변수 수정
# print("숫자 변환 = ",숫자바꾸기)
# 영어바꾸기 = re.sub("[A-z]", "*", 문자열이저장된변수) # 규칙[가-힣]에 일치하는 글자 찾아서 바꿀글자[^^]로 문자열이 저장된 변수 수정
# print("영어 변환 = ",영어바꾸기)
#
# # 특정문자가 아닌 문자를 찾아서 삭제
# 숫자바꾸기 = re.sub("[^0-9]", "", 문자열이저장된변수) # 규칙[가-힣]에 일치하는 글자 찾아서 바꿀글자[^^]로 문자열이 저장된 변수 수정
# print("숫자만 남기고 및 특정문자 아닌 문자 삭제 = ",숫자바꾸기)
# 영어바꾸기 = re.sub("[^A-z]", "", 문자열이저장된변수) # 규칙[가-힣]에 일치하는 글자 찾아서 바꿀글자[^^]로 문자열이 저장된 변수 수정
# print("영어만 남기고 특정문자 아닌 문자 삭제 = ",영어바꾸기)
#
# # 특정문자 바꾸기
# 특정문자바꾸기 = re.sub("이걸", "요걸", "이걸 바꾼다고") #
# print("특정문자 변환 = ",특정문자바꾸기)
#
# # re.replace 이용한 특정 문자 변환
# 문자열2 = "안녕하세요Helloこんにちは"
# 변신=문자열2.replace("こんにちは", "")
# print(변신)

import pandas as pd
df = pd.DataFrame({
    "name" : ["1번","2번","3번","4번","5번"],
    "score" : [90, 80, 100, 80, 95]
    })

# print("df",df)
# print("#"*80)
# print("score 칸만 출력\n", df["score"])
# print("#"*80)

# map 을 알기 前
print("score 칸 리스트 변환\n", df["score"].tolist())

리스트 = []
for i in df["score"].tolist():
    리스트.append(i+5)

print(리스트)
df["score"] = 리스트 # 리스트 값을 score에 넣어 값 갱신
print("df", df)

# map 을 알고난 後
def 학생점수올리는함수 (s):
    print("함수 호출")
    print("s=",s)
    # print("*"*80)
    return s+5
# map 함수 이용
# df["score"] = df["score"].map(학생점수올리는함수)  # map은 표에 사용된다.
# df["표의 칸"].map(함수)
# 표의 칸에서 순서대로 값하나씩 꺼내 함수에 대입함.

df["score"] = df["score"].apply(학생점수올리는함수)  # map은 표에 사용된다.
# map 을 이용해도 apply를 이용해도 결과는 같다.
print(df)