from flask import Flask
from flask import jsonify

server = Flask(__name__)


@server.route('/')
def home():
    return "Hello"


@server.route('/chat/<string:username>')
def chat(username):
    messages = ["Hello", "How are you?"]
    return jsonify(messages)


server.run(debug=True, host='0.0.0.0')
