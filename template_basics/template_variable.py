from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'John'
    letters = list(name)
    names = {1:'john', 2:'Jonny'}
    return render_template('temp_variable.html', name = name, letter = letters, names = names)

if __name__ == '__main__':
    app.run(debug= True)


