import os
from flask import Flask, render_template, redirect, url_for, request
import sqlite3

 # DB 연결
def dbcon():
    return sqlite3.connect('./mydb.db')

def create_db():
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE member (id varchar(50), passwd varchar(50))")
        c.execute("INSERT INTO member VALUES ( admin, admin)")
        db.commit()
    except Exception as e:
        print('db error: ',e)
    finally:
        db.close()
        
def insert_data(id, passwd):
    try:
        db = dbcon()
        c = db.cursor()
        #setdata = (id,passwd)
        c.execute("INSERT INTO member VALUES (" + id + "," + passwd + ")")
        db.commit()
        data = c.fetchall()
    except Exception as e:
        print('db error [inesert_data()] : ', e)
    finally:
        
        db.close()
        return data

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
    
def select_id(id):
    ret = ()
    try :
        db = dbcon()
        c = db.cursor()
        #setdata = (id, )
        c.execute('SELECT * FROM member WHERE id = ' + id)
        ret = c.fetchall()
    except Exception as e:
        print('db error [selct_id()] : ',e)
    finally:
        db.close()
        return ret
 

app = Flask(__name__)

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
        # sql 연결 및 실행
        db = dbcon()
        c = db.cursor()
        query = "INSERT INTO member VALUES ( '" + id + "','" + pwd + "','" + name + "')"
        print(query)
        c.execute(query)
        data = c.fetchall()
        if not data:
            db.commit()
            print('register Success!')
            return redirect(url_for('index'))
        else:
            db.rollback()
            return "Register Failed"

    return render_template('register.html', error=error)

if __name__ == "__main__":
    conn = dbcon()
    print ("Opened database successfully")
    conn.execute('CREATE TABLE IF NOT EXISTS member (id varchar(50), passwd varchar(50), nickname varchar(50))')
    print ("Table created successfully")
    conn.close()
    app.run()
   