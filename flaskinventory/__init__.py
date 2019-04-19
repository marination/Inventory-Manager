from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = '323b22caac41acbf'
app.config['SQLALCHEMY'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskinventory import routes

db.create_all()
db.session.commit()
