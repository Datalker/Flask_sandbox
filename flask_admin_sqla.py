from flask import Flask, url_for, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from alchemy import Person, Status

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

# Flask and Flask-SQLAlchemy initialization here

engine = create_engine('sqlite:///twittet_app.sqlite', echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()


admin = Admin(app, name='microblog', template_mode='bootstrap3')

class StatusView(ModelView):
    can_view_details = True


admin.add_view(ModelView(Person, session))
admin.add_view(StatusView(Status, session))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RTasdfa'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


