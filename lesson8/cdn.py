from flask import Flask, send_file, make_response
app = Flask(__name__)

@app.route('/')
def serve_file():
    resp = make_response(send_file('fb.png'))
    resp.headers['X-Access-Control-Allow-Origin'] = 'mybank.com'
    # resp.headers['Set-Cookie'] = 'eyal=1000;'
    return resp 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('cdn.crt', 'cdn.key'))