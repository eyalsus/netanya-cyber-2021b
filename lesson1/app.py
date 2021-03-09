from flask import Flask, render_template, request
app = Flask(__name__)


user_database = [
    {'username': 'alice', 'password': '1234'},
    {'username': 'bob', 'password': '2345'}
]

@app.route('/enter/')
def enter(name=None):
    return render_template('login.html', name=name)

@app.route('/login')
def login():
    response = 'ACCESS DENIED'
    username = request.args.get('username')
    password = request.args.get('password')
    for user in user_database:
        if username == user['username'] and password == user['password']:
            response = f'Hello {username}'
            break
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