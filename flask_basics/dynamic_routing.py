from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/info/<name>')
def info(name):
    return f'Information of {name}'


if __name__ == '__main__':
    app.run(debug= True)