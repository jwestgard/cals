from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/meals')
def meals():
    return "Enter meal info here"

@app.route('/foods')
def foods():
    return "List foods here"

if __name__ == "__main__":
    manager.run()
