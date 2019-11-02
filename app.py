from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from twilio import twiml

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User_db (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)