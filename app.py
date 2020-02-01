from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'flask quickstart'
    return render_template('index.html', title=title)

@app.route('/home')
def home():
    return "HOME"

@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/hello/<name>')
def greeting(name):
    return f"Hello {name}!"

@app.route('/post/<int:id>')
def post(id):
    return f"get the id: {id}"

