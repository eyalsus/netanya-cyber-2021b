import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

user_database = [
    {'username': 'alice', 'password': '1234'},
    {'username': 'bob', 'password': '2345'}
]

limit_failed_attpemts = {}

ACCESS_DENIED = 'ACCESS DENIED'


@app.route('/enter/')
def enter(name=None):
    return render_template('login.html', name=name)

@app.route('/login', methods=['POST'])
def login():
    response = ACCESS_DENIED

    if request.remote_addr in limit_failed_attpemts and limit_failed_attpemts[request.remote_addr] > 3:
        print('possible brute force detected')
    else:
        if request.user_agent.string.startswith('Mozilla'):
            username = request.form.get('username')
            password = request.form.get('password')
            with sqlite3.connect('users.db') as con:
                cur = con.cursor()
                cur.execute(f"select count(1) from users where username = '{username}' and password = '{password}'")
                count = cur.fetchone()[0]
                print(count)
                if count > 0:
                    cur.execute(f"select favorite_number from users where username = '{username}'")
                    favorite_number = cur.fetchone()[0]
                    response = f'Hello {username}\n your favorite number is {favorite_number}'
            # for user in user_database:
            #     if username == user['username'] and password == user['password']:
            #         response = f'Hello {username}'
            #         break
        else:
            print('not supported browser ')

        if response == ACCESS_DENIED:
            if request.remote_addr in limit_failed_attpemts:
                limit_failed_attpemts[request.remote_addr] += 1
            else:
                limit_failed_attpemts[request.remote_addr] = 1

    return response


@app.route('/')
def hello_world():
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
    app.run(port=80)