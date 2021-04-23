
from flask import Flask # Flask 객체 생성
from flask import render_template
app = Flask(__name__)   # app 파일호출, 확장자는빼고 실행파일 이름이 name이 파일 이름이된다.

@app.route("/")         # url 입력 :  http://127.0.0.1:5000/ 하면 이렇게 실행도미
def hello_pybo():       # 실행
    return "AWS 연습중입니다"

@app.route("/SelectFile") # url 입력 http://127.0.0.1:5000/selectFile 실행시 template 실행됨
def select_file():
    # return "url에 /slectFile 썼니?"
    return render_template("SelectFile.html")

# 파일업로드 html에서 입력값 처리
from flask import request

# AWS의 s3랑 연동하게 돕는 도우미
import boto3 # 사용하지 않으면 회색으로 보인다
from os import path
@app.route("/UploadFile", methods = ["POST"]) # 파일 업로드는 포스트 방식으로만

def upload_file():
    # 업로드 파일명 출력
    # print("request.files = ",request.files)
    # print("request.files['select'] = ", request.files['select'])
    # print("request.files['select'].filename = ", request.files['select'].filename) # 파일명만 보고싶을 때

    if request.method == 'POST':
        file = request.files['select']
        print("file.filename = ", file.filename)

        if file.filename != '':
            save_file_name = file.filename
            print("save_file_name = ",save_file_name)
            # print("같은 이름의 파일 이미 존재",path.exists("./temporary/"+save_file_name))
            count = 1
            while path.exists("./temporary/"+save_file_name) :
                print("같은 이름의 파일이 없을때 까지 반복 함")
                print("파일명과 확장자 분리 함",path.splitext(save_file_name))
                if len( path.splitext(save_file_name)) == 2 : # 나눠진게 2개이면
                    file_name, ext = path.splitext(save_file_name) # save_file_name 이 split하여 file_name과 ext에 넣어 저장된다.
                    print("file =",file_name)
                    print("ext =",ext)

                else :
                    file_name = save_file_name
                    ext = ""

                save_file_name = file_name + str(count) + ext
                print("새로운 파일명 = ", save_file_name)
                count = count + 1

                # break

            print("save_file_name = " , save_file_name)
            file.save("./temporary/"+save_file_name)    # ./ 는 현재 폴더를 의미하고 지금 현재 위치는 c:\\projects\\myproject 이다
            print("temporary에 파일 저장함")

            s3 = boto3.client("s3") # s3랑 pybo.py 연결해서  작업 객체 생성 리턴하여 s3 저장
            s3.upload_file("./temporary/"+save_file_name,"pblamj",save_file_name)
            return save_file_name+"을 버켓에 업로드 완료"

    return "s3 파일 업로드 실패" # 리턴 위치 중요



@app.route("/ViewFileList") # @ 어노테이션 ()안의 내용이 들어올때 아래 함수를 실행
def view_file_list():

    s3 = boto3.client('s3') # boto를 이용해 어디든지 접속가능하고 s3에 접속 하겠다면 괄호안에 명시
    paginator = s3.get_paginator("list_objects_v2") # 데이터를 가져올 객체 생성
    # paginator.paginate(Bucket = "pblamj")
    response_iterator = paginator.paginate(Bucket = "pblamj")
    # print("response_iterator = ",response_iterator)
    # print("list(response_iterator) = ", list(response_iterator) )
    file_list = list(response_iterator)
    # print("file_list[0] = ", file_list)
    # print("=" * 100)
    # print("file_list[0] = ", file_list[0])
    # print("*" * 100)
    print("file_list[0] 에서 지울거 지우고= ", file_list[0]["Contents"])


    return render_template("/ViewFileList.html",file_list= file_list[0]["Contents"]) # html 불러오기

from flask import Response  # 파일 내용을 브라우저에 출력하지 않고 파일 자체 전송

import urllib


@app.route("/DownloadFile", methods=["POST"]) # 방화벽을 풀어줘야 하기에 methods를 통해
def download_file():
    file_name = request.form["hahaha"]
    print("request.form = ", request.form)
    # print("request.form["hahaha"] = ", request.form["hahaha"])
    file_name = request.form["hahaha"]

    s3= boto3.client("s3")
    file_downloder = s3.get_object(Bucket="pblamj",Key=file_name)

    print("file_downloader = ", file_downloder)
    print("="*100)

    print("file_downloder['Body'].read()")
    print(file_downloder['Body'].read() )
    print("=" * 100)


    # return file_name + " 오른쪽에 있는 버튼 눌림"
    # return file_downloder['Body'].read() # 파일 내용에 브라우저가 출력됨
    favorite_youtube_channel = "애주가 참피디.txt"
    # print("애주가 참피디 숫자로 변환 encoding = ", favorite_youtube_channel.encode("utf-8"))
    encode=file_name.encode("utf-8")
    print("encode = " , encode)
    encode_remove_space = urllib.parse.quote(encode)
    print("encode_remove_space = ", encode_remove_space)
    return Response(
        file_downloder["Body"].read() ,
        headers={
            "Content-Disposition":"attachment;filename="+encode_remove_space
        } # 다운로드시 저장될 파일명이 mac_pro.txt로 저장됨
    )