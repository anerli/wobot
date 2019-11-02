from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from twilio_tools import send_message
from flask_apscheduler import APScheduler
import schedule_tools
import time

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
scheduler = APScheduler()
scheduler.init_app(app)


class User_db (db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # string of 1's and 0's in a particular order to denote which muscle groups have been used
    # '10' is number muscle groups
    last_worked_mgroups = db.Column(db.String(10), default='1111100000')
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #msg = request.form['msg']
        #num = request.form['num']
        #send_message(msg, num)

        phone_number = request.form['phone_number']
        # etc...
        
        return redirect('/')
    else:
        return render_template('index.html')

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

if __name__ == '__main__':
    #schedule_tools.schedule_the_message_send_scheduler(scheduler)
    #scheduler.add_job(func=print_date_time, trigger="interval", seconds=3, id='dateprinter')
    scheduler.add_job(func=lambda: schedule_tools.schedule_message_sends(scheduler, ), trigger="cron", hour=0, id='dateprinter')
    scheduler.start()

    # Remember to take off debug mode on upload. This also fixes sheduler running things twice
    app.run(debug = True)
    
