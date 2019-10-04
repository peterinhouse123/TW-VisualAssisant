#用來接收消息用的
from flask import Flask

app = Flask(__name__)

Services = None



@app.route('/')
def home():
    return "ready!"

@app.route('/push/<message>')
def push(message):
    rs = Services.push(message)

    return rs


if __name__ == '__main__':
    app.run()