import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)


def connect():
    """ Connect to MySQL database """

    conn = mysql.connector.connect(host='localhost',
                                   database='mydata',
                                   user='root',
                                   password='pass')

    return conn


@app.route('/login/verify', methods=['POST'])
def login_verify():
    conn = connect()

    user = 0
    passwd = 0

    if request.method == 'POST':
        user = request.form.get('username')
        passwd = request.form.get('password')

    cur = conn.cursor()
    q = "SELECT * FROM mydata.tbl WHERE Username = '**' AND Password = '*/';".replace("**", user).replace("*/", passwd)
    cur.execute(q)

    if cur.fetchall():
        return render_template('LoginApproved.html')
    else:
        return render_template('LoginFailed.html')


@app.route('/login')
def login():
    return render_template('LoginScreen.html')


@app.route('/login/failed', methods=['GET', 'POST'])
def login_failed():
    failed = 1
    return render_template('LoginScreen.html', failed=failed)


@app.route('/')
def home():
    return render_template('LoginRedirect.html')


if __name__ == '__main__':
    app.run()
