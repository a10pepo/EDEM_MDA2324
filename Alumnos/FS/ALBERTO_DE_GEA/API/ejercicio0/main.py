from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'My First Web in Flask!'

app.run(host='0.0.0.0', port=99)