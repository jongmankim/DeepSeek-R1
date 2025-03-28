from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello docker world!'

app.run(host='0.0.0.0', port=8888)