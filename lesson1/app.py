from flask import Flask, render_template, request
app = Flask(__name__)


user_database = [
    {'username': 'alice', 'password': '1234'},
    {'username': 'bob', 'password': '2345'}
]


# @app.route('/login'):


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