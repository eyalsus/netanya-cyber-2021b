import sqlite3
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

user_database = [
    {'username': 'alice', 'password': '1234'},
    {'username': 'bob', 'password': '2345'}
]

limit_failed_attpemts = {}

@app.route('/enter/')
def enter(name=None):
    sso_username = request.cookies.get('SSO')
    if sso_username:
        favorite_number = request.cookies.get('favorite_number')
        return render_template('loggedin_user.html', username=sso_username, favorite_number=favorite_number)
    return render_template('login.html', name=name)

@app.route('/login', methods=['POST'])
def login():
    ACCESS_DENIED = make_response(render_template('not_allowed.html'))
    resp = ACCESS_DENIED

    if request.remote_addr in limit_failed_attpemts and limit_failed_attpemts[request.remote_addr] > 3:
        print('possible brute force detected')
    elif not (request.referrer.startswith('http://mybank.com/enter') or request.referrer.startswith('https://mybank.com/enter')):
        print('possible CSRF attack')
    else:
        if request.user_agent.string.startswith('Mozilla'):
            username = request.form.get('username')
            password = request.form.get('password')
            chkbox = request.form.get('chkbox')
            with sqlite3.connect('users.db') as con:
                cur = con.cursor()
                # cur.execute(f"select count(1) from users where username = '{username}' and password = '{password}'")
                t = (username, password)
                print(f'username: {username}, password: {password}')
                cur.execute(f"select count(1) from users where username = ? and password = ?", t)
                count = cur.fetchone()[0]
                print(f'matching users found: {count}')
                if count > 0:
                    cur.execute(f"select favorite_number from users where username = '{username}'")
                    favorite_number = cur.fetchone()[0]
                    resp = make_response(render_template('loggedin_user.html', username=username, favorite_number=favorite_number))
                    
                    if chkbox == 'on':
                        resp.set_cookie('SSO', value=username, max_age=3600)
                        resp.set_cookie('favorite_number', value=str(favorite_number), max_age=3600)
                    
                    # response = f'Hello {username}, your favorite number is {favorite_number}'
            # for user in user_database:
            #     if username == user['username'] and password == user['password']:
            #         response = f'Hello {username}'
            #         break
        else:
            print('not supported browser ')

        if resp == ACCESS_DENIED:
            if request.remote_addr in limit_failed_attpemts:
                limit_failed_attpemts[request.remote_addr] += 1
            else:
                limit_failed_attpemts[request.remote_addr] = 1

    return resp


@app.route('/')
def hello_world():
    from time import sleep
    sleep(10)
    return 'Hello, World!<script>alert("Hi")</script>'

@app.route('/user/<user>', methods=['GET', 'POST'])
def hello_user(user):
    return f'<h3>Hello, <b>{user}!</b></h3>'

@app.route('/cyber')
def hello_cyber_b():
    name = request.args.get('name')
    return f'Hello {name}, Welcome to Cyber B!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('server.crt', 'server.key'))