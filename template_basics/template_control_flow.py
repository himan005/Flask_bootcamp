from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    my_list = ['Banana', 'Mango', 'Water Melon']
    return render_template('control_flow.html', mylist = my_list )

if __name__ == '__main__':
    app.run(debug = True)

