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
    #id = db.Column(db.Integer, primary_key=True)

    # string of 1's and 0's in a particular order to denote which muscle groups have been used
    # '10' is number muscle groups
    last_worked_mgroups = db.Column(db.String(10), default='1111100000')

    phone_number = db.Column(db.String(10), primary_key=True)
    difficulty = db.Column(db.String())
    goal = db.Column(db.String())
    time = db.Column(db.Integer)
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #msg = request.form['msg']
        #num = request.form['num']
        #send_message(msg, num)

        # 
        #User_db.query.get_or_404()

        # new user settings
        new_user_settings = User_db()
        new_user_settings.phone_number = request.form['phone_number']
        new_user_settings.difficulty = request.form['difficulty']
        new_user_settings.goal = request.form['goal']
        new_user_settings.time = request.form['time']

        #print(new_user_settings.phone_number)

        #exists = db.session.query(User_db.phone_number).filter_by(phone_number=new_user_settings.phone_number).scalar() is not None
        #exists = db.session.query(db.exists().where(User_db.phone_number == new_user_settings.phone_number)).scalar()
        #exists = User_db.query(User_db.query.exists().where(User_db.phone_number == new_user_settings.phone_number)).scalar()

        #q = User_db.query.filter(User_db.phone_number == new_user_settings.phone_number)
        #print(q)
        #if(User_db.query(q.exists())):
        #if exists:
            # New user is already in database, just remove that entry so we can add it again
            #db.session.remove()
        User_db.query.filter(User_db.phone_number == new_user_settings.phone_number).delete()
        

        schedule_tools.schedule_message_sends(scheduler, new_user_settings)

        db.session.add(new_user_settings)
        db.session.commit()

        

        # etc...

        return redirect('/')
    else:
        return render_template('index.html')

#@app.route('/update_worked_mgroups', methods=['POST'])
'''
Called by schedule_tools
'''
def update_worked_mgroups(phone_number, new_worked_mgroups):
    pass


def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

if __name__ == '__main__':
    #schedule_tools.schedule_the_message_send_scheduler(scheduler)
    #scheduler.add_job(func=print_date_time, trigger="interval", seconds=3, id='dateprinter')

    scheduler.add_job(func=lambda: schedule_tools.schedule_message_sends(scheduler, User_db.query.all()), trigger="cron", hour=0, id='dateprinter')
    scheduler.start()

    # Remember to take off debug mode on upload. This also fixes sheduler running things twice
    app.run(debug = True)
    
