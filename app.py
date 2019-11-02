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

@app.route('/sms',methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)


if __name__ == '__main__':
    app.run(debug = True)