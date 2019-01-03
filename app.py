from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'this is my_first flask, say hello world!'

app.run()
