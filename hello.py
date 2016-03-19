from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<H1>Hello world!!!!</H1>'


@app.route('/user/<username>')
def user(username):
    s = 'Hello <a href="{1}"> <H1>{0}</H1> </a>'
    return s.format(username, url_for('static', filename='flask_freeze.txt'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
