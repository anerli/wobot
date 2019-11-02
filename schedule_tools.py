import msg_gen
from datetime import datetime
import twilio_tools
import time
from app import update_worked_mgroups

'''
Run once when server up

def schedule_the_message_send_scheduler(scheduler):
    pass
'''

'''
Need to schedule this for every day, and w user setting call every time user changes or adds a settings

Run on new usersetting whenever one is added or changed
Run on all usersettings every day

Takes in the db's us

Return new lask_worked_mgroups string
'''
def schedule_message_sends(scheduler, usersettingsarr):
    print(usersettingsarr)

    

    for usersettings in usersettingsarr:
        msg, new_worked_mgroups = msg_gen.workout(usersettings.last_worked_mgroups,usersettings.difficulty,usersettings.goal)

        num = usersettings.phone_number
        time = usersettings.time


        #time = [h1, h2, m1, m2]

        hour = str(time[0]) + str(time[1])
        minute = str(time[2]) + str(time[3])


        scheduler.add_job(func=lambda: twilio_tools.send_message(msg, num), \
            trigger="date", run_date=datetime(datetime.now[0], datetime.now[1], datetime.now[2], hour, minute, 0))
        
        update_worked_mgroups(num, new_worked_mgroups)

        

    #return new_worked_mgroups
    