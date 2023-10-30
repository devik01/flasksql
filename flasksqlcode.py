from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'deviflasksql'

mysql = MySQL(app)

@app.route('/')
def func1():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST' and 'uname' in request.form and 'pass' in request.form:
        username = request.form['uname']
        password = request.form['pass']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usertable WHERE user_id=%s AND password_user=%s", (username, password))
        account = cursor.fetchone()
        if account:
            return redirect(url_for("success"))
        else:
            return redirect(url_for("fail"))

@app.route('/success')
def success():
    return "Success!"

@app.route('/fail')
def fail():
    return "Unsuccessful"

if __name__ == '__main__':
    app.run(debug=True)
