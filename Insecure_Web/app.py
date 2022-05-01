from datetime import timedelta
import sys,os
from tkinter import EXCEPTION
from flask import Flask, render_template, redirect, url_for, request, flash, session
import sqlite3
import html

 # DB  연결
def dbcon():
    return sqlite3.connect(os.path.dirname(os.path.realpath(__file__))+'/mydb.db')

# 실행 시 DB 초기화
def create_db():
    try:
        conn = dbcon()
        print ("Opened database successfully")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS member (id varchar(50) PRIMARY KEY NOT NULL, passwd varchar(50) NOT NULL, nickname varchar(50) NOT NULL)')
        print ("'member' Table created successfully")
        query = '''CREATE TABLE IF NOT EXISTS board (
        num INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT NOT NULL,title TEXT NOT NULL, 
        content TEXT, 
        reg_date DATETIME DEFAULT (datetime('now','localtime'))) '''
        c.execute(query)
        print ("'board' Table created successfully")
        c.execute("INSERT INTO member VALUES ( 'admin', 'admin','admin')")
        print ("Insert Admin")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('HELLO','THIS_IS','TEST_CONTENT')")
        c.execute("INSERT INTO board (id,title,content) VALUES ('Java','script','<script>alert(1);</script>')")
        print("Insert Test data")
        conn.commit()
    except Exception as e:
        print('db error: ',e)
    finally:
        conn.close()

# Register를 통해 DB에 데이터 삽입
def insert_data_member(id, passwd, nickname):
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("INSERT INTO member (id,passwd,nickname) VALUES (%(id)s  ,  %(passwd)s,  %(nickname)s)",{
            'id':id,
            'passwd':passwd,
            'nickname':nickname
        })
        db.commit()
        c.fetchall()
        print("Insert data() : id=" + id + "\tpassword = "+ passwd + "\tname = " + nickname)
    except Exception as e:
        print('db error [insert_data_member()] : ', e)
        db.rollback()
        db.close()
        return False
    else:
        db.close()
        return True


# 로그인 시 id, passsword 확인 함수
def check_passwd(id,input_passwd):
    print("check_passwd call")
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("SELECT id, passwd from member WHERE id=%(id)s AND passwd =%(input_passwd)s ",(id,input_passwd))
        print("execute")
        
        rows = c.fetchall()
        print("fetchall")
        print("입력한 id = ",id,"입력한 password = ",input_passwd)
        # 쿼리 결과문이 리스트로 나오기에 for문
        for rs in rows:
            print(id,'의 비밀번호는 ', rs[1],'입니다')
            if id == rs[0] and input_passwd == rs[1]:
                print("login Success")
                return True
            else:
                print("login failed")
                return False
    except Exception as e:
        print('db error [check_passwd()] : ',e)

# 글 읽기
def read_post(num):
    print("read_post call")
    try:
        db = dbcon()
        c = db.cursor()
        query = f"SELECT * FROM board WHERE num = {num};"
        c.execute(query)
        rows = c.fetchone()
        print("해당 글 ",rows)
        c.close()
        if rows == None:
            return False
        return rows
    except Exception as e:
        print('db error [read_post()] : ',e)

# 글 작성 함수
def insert_data_board(id, subject, content):
    try:
        db = dbcon()
        print ("Opened database successfully")
        c = db.cursor()
        query = f"INSERT INTO board (id,title,content) VALUES (' {id} ',' {subject} ',' {content}')"
        c.execute(query)
        db.commit()
        c.fetchall()
    except Exception as e:
        print('db error [insert_data_board()] : ', e)
        db.rollback()
        db.close()
        return False
    else:
        db.close()
        return True

# 글 삭제 함수
def delete(idx):
    try:
        db = dbcon()
        c = db.cursor()
        query= f"DELETE FROM board WHERE num = {idx}"
        print("1")
        print(idx)
        c.execute(query)
        db.commit()
        c.fetchall()
        print("delete() : fetchall")
    except Exception as e:
        print('db error [delete_data_board()] : ',e)
        db.rollback()
        db.close()
        return False
    else:
        db.close()
        return True

# 글 삭제 시 id 체크 함수
def check_id(id,idx):
    try:
        if id == 'admin':
            print("check_id : admin")
            return True
        db = dbcon()
        c = db.cursor()
        query= F"SELECT id FROM board WHERE num = {idx}"
        c.execute(query)
        value = c.fetchall()
        for rs in value:
            print("출력 id = ",rs[0],"\t 입력온 id = ",id)
            db.close()
            if rs[0] == id:
                print("check_id : True")
                return True
            else:
                print("check_id : False")
                return False
    except Exception as e:
        print('db error [check_id()] : ',e)
        db.close()
        return False
                
app = Flask(__name__)
app.secret_key = 'this is secret key'
# 세션 지속 시간 10분
app.config["PERMANET_SESSION_LIFETIME"] = timedelta(minutes=10)

# index page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# 로그아웃 구현
@app.route('/logout')
def logout():
    # logout and redirect ro index page
    session.pop("userid",None)
    flash("로그아웃 완료")
    return redirect(url_for('index'))

# 로그인 후 첫 페이지
@app.route('/homepage')
def homepage():
    # 게시판 등 로그아웃 구현
    userid = session.get('userid',None)
    if 'userid' in session:
        flash("환영합니다! " + userid + '님')
    return render_template('homepage.html', userid=userid)


# 로그인 화면
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('username')
        passwd = request.form.get('password')
        if check_passwd(id,passwd):
            session['userid'] = id
            return redirect(url_for('homepage'))
        else:
            flash('정보가 틀립니다')
            return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('login.html')
    return render_template('login.html')

# 회원가입 화면
@app.route('/register',methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form.get('reg_id')
        pwd = request.form.get('reg_passwd')
        name = request.form.get('name')
        if not (id and pwd and name):
            flash("빈칸이 존재합니다")
            return redirect(url_for('register'))
        if insert_data_member(id,pwd,name):
            print('register Success!')
            return redirect(url_for('index'))
        else:
            flash(id + "가 존재하거나 sql injection 시도가 있습니다")
            return redirect(url_for('register'))


    return render_template('register.html', error=error)

# no filter board page
@app.route('/board',methods=['GET'])
def board():
    if 'userid' not in session:
        flash("로그인이 필요합니다!")
        return redirect(url_for('index'))
    error = None
    # 세션으로 로그인 유저 아이디 저장
    id = session['userid']
    conn = dbcon()
    cursor = conn.cursor()
    sql = "SELECT * FROM board ORDER BY reg_date desc"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    data_list = []
    # id, title, content, reg_data
    for obj in data:
        data_dic = {
            'num' : obj[0],
            'id' : obj[1],
            'title' : obj[2],
            'content' : obj[3],
            'time' : obj[4]
        }
        data_list.append(data_dic)
    cursor.close()
    conn.close()
    
    return render_template('board.html', error=error, name=id, data_list= data_list)
    
@app.route('/board/<int:num>', methods=['GET','POST'])
def board_vew(num):
    if 'userid' not in session:
        flash("로그인이 필요합니다!")
        return redirect(url_for('index'))
    
    id = session['userid']
    
    if request.method == 'POST':
        idx = request.values.get('idx')
        if check_id(id,idx):    
            if delete(idx):
                flash("삭제가 완료되었습니다!")
                return redirect(url_for('board'))
        else:
            flash("글 쓴 id 또는 admin 계정으로만 삭제가 가능합니다.")
            return redirect(url_for('board'))
        
    post = read_post(num)
    if post == False:
        flash("해당 글은 존재하지 않습니다!")
        return redirect(url_for('board'))
    data_dic = {
        'num' : post[0],
        'id' : post[1],
        'title' : post[2],
        'content' : post[3],
        'time' : post[4]
    }
    print(post)
    print(post[3])
    print(type(post[3]))
    return render_template('board_view.html',data = data_dic)

# 글 작성
@app.route('/board/write',methods=['GET','POST'])
def board_write():
    if 'userid' not in session:
        flash("로그인이 필요합니다!")
        return redirect(url_for('index'))
    id = session['userid']
    if request.method == 'GET':
        return render_template('board_write.html')
    elif request.method=="POST":
        subject = request.form['subject']
        content = request.form['contents']
        print("작성자 :",id,"\t 제목 :",subject,"\t 내용 :",content)
        # ckeditor에서는 기본적으로 <script>를 넣을 못 넣게 되어 있음.
        # <script>alert(1);</script> 를 넣을 경우 아래와 같은 방식으로 치환됨
        # &lt;script&gt;alert(1);&lt;/script&gt;
        # 따라서 html.unescape문을 통해 변환 후 db에 저장
        unescape_subject = html.unescape(subject)
        unescape_content = html.unescape(content)
        if insert_data_board(id,unescape_subject,unescape_content):
            print('글 작성 완료')
        else:
            flash("글 작성 오류!")
        return redirect(url_for('board'))




# low level filter board
@app.route('/low_board',methods=['GET'])
def low_board():
    error = None
    # 세션으로 로그인 유저 아이디 저장
    id = session['userid']
    conn = dbcon()
    cursor = conn.cursor()
    sql = "SELECT * FROM low_board ORDER BY reg_date desc"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    data_list = []
    # id, title, content, reg_data
    for obj in data:
        data_dic = {
            'num' : obj[0],
            'id' : obj[1],
            'title' : obj[2],
            'content' : obj[3],
            'time' : obj[4]
        }
        data_list.append(data_dic)
    cursor.close()
    conn.close()
    
    return render_template('low_board.html', error=error, name=id, data_list= data_list)
    
@app.route('/low_board/<int:num>')
def low_board_vew(num):
    post = read_post(num)
    if post == False:
        flash("해당 글은 존재하지 않습니다!")
        return redirect(url_for('low_board'))
    data_dic = {
        'num' : post[0],
        'id' : post[1],
        'title' : post[2],
        'content' : post[3],
        'time' : post[4]
    }
    print(post)
    print(post[3])
    print(type(post[3]))
    return render_template('low_board_view.html',data = data_dic)

if __name__ == "__main__":
    create_db()
    app.run()
   