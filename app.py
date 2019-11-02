from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from twilio_tools import send_message

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User_db (db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # string of 1's and 0's in a particular order to denote which muscle groups have been used
    # '10' is number muscle groups
    last_worked_mgroups = db.Column(db.String(10))
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form['msg']
        num = request.form['num']
        send_message(msg, num)
        return redirect('/')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)