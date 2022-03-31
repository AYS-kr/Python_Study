import sys,os
from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3


 # DB 연결
def dbcon():
    return sqlite3.connect(os.path.dirname(os.path.realpath(__file__))+'/mydb.db')

# 실행 시 DB 초기화
def create_db():
    try:
        conn = dbcon()
        print ("Opened database successfully")
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS member (id varchar(50) PRIMARY KEY NOT NULL, passwd varchar(50) NOT NULL, nickname varchar(50) NOT NULL)')
        print ("Table created successfully")
        c.execute("INSERT INTO member VALUES ( 'admin', 'admin','admin')")
        print ("Insert Admin")
        conn.commit()
    except Exception as e:
        print('db error: ',e)
    finally:
        conn.close()

# Register를 통해 DB에 데이터 삽입
def insert_data(id, passwd, name):
    try:
        db = dbcon()
        c = db.cursor()
        query = "INSERT INTO member VALUES ( '" + id + "','" + passwd + "','" + name + "')"
        c.execute(query)
        db.commit()
        c.fetchall()
        print("Insert data() : id=" + id + "\tpassword = "+ passwd + "\tname = " + name)
    except Exception as e:
        print('db error [inesert_data()] : ', e)
        db.rollback()
        db.close()
        return False
    else:
        db.close()
        return True

# 나중에 사용 예정
def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM member')
        ret = c.fetchall()
    except Exception as e:
        print('db error [select_all()] : ',e)
    finally:
        db.close()
        return ret

# 나중에 사용 예정
def select_id(id):
    ret = ()
    try :
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM member WHERE id = ' + id)
        ret = c.fetchall()
    except Exception as e:
        print('db error [selct_id()] : ',e)
    finally:
        db.close()
        return ret
 

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/secret')
def secret():
    return "Secret"

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Try again'
        else:
            return redirect(url_for('secret'))
    return render_template('login.html',error=error)

@app.route('/register',methods=['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form.get('reg_id')
        pwd = request.form.get('reg_passwd')
        name = request.form.get('name')
        
        if insert_data(id,pwd,name):
            print('register Success!')
            return redirect(url_for('index'))
        else:
            flash("Register Failed")
            return redirect(url_for('register'))


    return render_template('register.html', error=error)

if __name__ == "__main__":
    dbcon()
    create_db()
    app.run()
   