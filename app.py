import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Puppy(db.Model):
    __tablename__ = "puppies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    breed = db.Column(db.text)

title = 'Flask with Database Relationships and Associations'

@app.route('/')
def index():
    return render_template('home.html', title=title)

@app.route('/about')
def about():
    return render_template('about.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html', title=title, e=e)

if(__name__) == '__main__':
    app.run(Debug=True)