from flask import Flask
import boto3
from flask import render_template
# render_template를 사용하는 이유는 html형식으로 뿌려줄거기 때문이다.

from flask import request
#입력한 값을 가져오는 객체 request

from flask import redirect, url_for

from decimal import Decimal


app = Flask(__name__)


@app.route('/')
def hello_student_manager():

    dynamodb = boto3.resource('dynamodb')   # dynamodb에 접속할 객체 생성되어 dynamodb에 저장

    table =dynamodb.Table('UnivStudent')    # UnivStudent 테이블에 레코드 추가, 수정, 삭제, 조회 할 객체 생성

    response = table.scan()                 # 이 명령어가 시작 될 때 위의 dynamodb,table이 진짜로 접속시작하고 전체 조회 하고 결과 리턴 됨

    print("response = ", response) # 필요없는 것 까지 받게됨

    print("response['Items'] = ", response['Items']) # 필요한 결과만 줄여 받는다

    return render_template('ViewStudentList.html', # html 실행 render_template 안에 있는 값만 html 으로 보내 줄 수있다.
        student_list=response['Items'])              # student list 라는 변수명과 repose['Items']라는 변수값에 저장하고 위의 'ViewStudentList.html' 에 정보 전달

@app.route('/AddStudentForm')
def add_student_form():

    return render_template('AddStudentForm.html')



@app.route('/AddStudent',methods=['POST']) # /AddStudent 를 POST 방식으로
def add_student():
    # 뭐가 들어가는지 궁금하면 print를 이용해 requeset.form[xxxx]을 출력하여 확인해 보면도니다.
    univ_id = request.form["univ_id"]
    univ_name = request.form["univ_name"]
    major = request.form["major"]
    circle = request.form["circle"]
    avg_credit = request.form["avg_credit"]


    # 학번이 입력된 univ_id와 이름이 입력된 univ_name 에 값이 꼭 입력되어야한다. primary key 이기 때문에
    if univ_id != ""and univ_name != "":  # ""의 의미는 입력하지 않았다.  id와 name을 입력하지 않았을때
        new_student = {
            'univ_id': Decimal(univ_id),  # 내가 숫자로 입력해도 플라스크는 문자로 받는다. 그러므로 type을 숫자타입으로 변경
            'univ_name': univ_name        # <form>에 입력한 값을 flask는 문자로 바꿔 받는다.
        }

        if major != "":
            new_student["major"] = major # major가 dictionary에 추가됨

        if circle != "":
            new_student["circle"] = circle # circle이 dictionary에 추가됨

        if avg_credit != "":
            new_student["avg_credit"] = Decimal(avg_credit)

        print("new_student = ", new_student) # 전체적인 new_student 상태 출력

        dynamodb = boto3.resource('dynamodb')  # dynamodb에 접속할 객체 생성되어 dynamodb에 저장

        table = dynamodb.Table('UnivStudent')  # UnivStudent 테이블에 레코드 추가, 수정, 삭제, 조회 할 객체 생성

        table.put_item(Item=new_student)       # dictionary 타입의  new_student를 dynamodb에 넣는다.

    return redirect(url_for('hello_student_manager'))  # 호출할 함수를 옆과 같은 형태로 부른다.



@app.route("/RemoveStudent", methods = ['POST'])
def remove_student():
    univ_name = request.form["univ_name"]
    print("univ_name = ", univ_name)

    univ_id = request.form["univ_id"]
    print("univ_id = ", univ_id)

    # dynamodb에 접속해 table 데이터 가져옴
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UnivStudent')

    will_remove_student = {
        'univ_name': univ_name,
        'univ_id': Decimal(univ_id)
    }
    print("will_remove_student", will_remove_student)
    table.delete_item(
        Key = will_remove_student
    )

    return redirect(url_for('hello_student_manager'))
