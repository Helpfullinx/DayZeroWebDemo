from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/login/verify', methods=['POST'])
def login_verify():
    file = (open(r"static/Accounts.txt", "r")).read()
    usernames = []
    passwords = []

    words = file.splitlines()
    for i in words:
        usernames.append(i.split(' ')[0])
        passwords.append(i.split(' ')[1])

    user = 0
    passwd = 0

    if request.method == 'POST':
        user = request.form.get('username')
        passwd = request.form.get('password')

    for i in range(len(usernames)):
        if user == usernames[i] and passwd == passwords[i]:
            return render_template('LoginApproved.html')

    return render_template('LoginFailed.html')


@app.route('/login')
def login():
    return render_template('LoginScreen.html')


@app.route('/')
def home():
    return render_template('LoginRedirect.html')


if __name__ == '__main__':
    app.run()
