from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from twilio_tools import send_message
from flask_apscheduler import APScheduler
import schedule_tools
import time
from datetime import datetime
import twilio_tools

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
scheduler = APScheduler()
scheduler.init_app(app)


class User_db (db.Model):
    #id = db.Column(db.Integer, primary_key=True)

    # string of 1's and 0's in a particular order to denote which muscle groups have been used
    # '10' is number muscle groups
    last_worked_mgroups = db.Column(db.String(10), default='0000000000')

    phone_number = db.Column(db.String(10), primary_key=True)
    difficulty = db.Column(db.String())
    goal = db.Column(db.String())
    time = db.Column(db.Integer)

    def __repr__(self):
        return "Last worked muscle groups: {}\nNum: {}\nDifficulty: {}\nGoal: {}\n Time: {}".format(\
            self.last_worked_mgroups, self.phone_number, self.difficulty, self.goal, self.time)
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Got POST request to /")
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
        
        #print("TIME: \n" + str(new_user_settings.time))
        #print(new_user_settings.time)
        #print("TIME1: \n" + str(new_user_settings.time[0]))
        #print("TIME2: \n" + str(new_user_settings.time[1]))

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
        
        #print("lwmg: " +  new_user_settings.last_worked_mgroups)
        #jank
        if not new_user_settings.last_worked_mgroups:
            new_user_settings.last_worked_mgroups = '0000000000'


        print("Scheduling message for " + str(new_user_settings.phone_number) + " at " + str(new_user_settings.time))
        nums, mgroups = schedule_tools.schedule_message_sends(scheduler, [new_user_settings])
        
        ##################
        # Update mgroup ##
        num = nums[0]
        new_worked_mgroups = mgroups[0]
        
        new_user_settings.last_worked_mgroups = new_worked_mgroups
        ###################

        db.session.add(new_user_settings)
        db.session.commit()
        
        

        # etc...

        #return redirect('success.html')
        return render_template('success.html', time=new_user_settings.time)
    else:
        return render_template('index.html')

#@app.route('/update_worked_mgroups', methods=['POST'])
'''
Called by schedule_tools
'''
def update_worked_mgroups(phone_number, new_worked_mgroups):
    #userset = User_db.query.filter(User_db.phone_number==phone_number).first()
    #userset.last_worked_mgroups = new_worked_mgroups
    #db.session.commit()
    pass


def print_date_time():
    print()
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def print_all():
    print(User_db.query.all())



def schedule_all():
    nums, mgroupsarr = schedule_tools.schedule_message_sends(scheduler, User_db.query.all())

    for i in range(len(nums)):
        num = nums[i]
        new_worked_mgroups = mgroupsarr[i]
        
        userset = User_db.query.filter(User_db.phone_number==num).first()
        userset.last_worked_mgroups = new_worked_mgroups
        db.session.commit()


if __name__ == '__main__':
    #schedule_tools.schedule_the_message_send_scheduler(scheduler)
    #scheduler.add_job(func=print_date_time, trigger="interval", seconds=3, id='dateprinter')

    #scheduler.add_job(func=lambda: schedule_tools.schedule_message_sends(scheduler, User_db.query.all()), trigger="cron", hour=0, id='dateprinter')
    scheduler.add_job(func=schedule_all, trigger="cron", hour=0, id='dateprinter')

    #scheduler.add_job(func=print_date_time, trigger='interval', seconds=5, id="timeprinter")
    #scheduler.add_job(func=print_all, trigger='interval', seconds=5, id="printer")


    
    #hour = 18
    #minute = 55
    # does not work nevermind does?
    #scheduler.add_job(func=lambda: twilio_tools.send_message("\nThis is a test\n", "3195411516"), \
    #        trigger="date", id="testthing", run_date=datetime(int(datetime.now().year), int(datetime.now().month), int(datetime.now().day), int(hour), int(minute), 0))
    
    #print("AAAAAAAAAAAAAAAAAA")

    scheduler.start()



    # Remember to take off debug mode on upload. This also fixes sheduler running things twice
    app.run(debug = True)
    #app.run(debug = True)
    
