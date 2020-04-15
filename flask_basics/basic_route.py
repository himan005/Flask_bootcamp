from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page'

@app.route('/info')
def info():
    return 'Information page'

if __name__ == '__main__':
    app.run()