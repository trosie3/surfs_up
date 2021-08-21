# import dependency 
from flask import Flask

# flask app instance
app = Flask(__name__)

# app route
@app.route('/')
def hello_world():
    return 'Hello world'

# skill drill another route
@app.route('/hello')
def hello():
    return 'Hello, World. I am learing'
