'''
Run once when server up
'''
def schedule_the_message_send_scheduler(scheduler):
    pass


'''
Need to schedule this for every day, and w user setting call every time user changes or adds a settings

Run on new usersetting whenever one is added or changed
Run on all usersettings every day

Takes in the db's us

Return new lask_worked_mgroups string
'''
def schedule_message_sends(scheduler, usersettingsarr):
    print(usersettingsarr)

    new_last_work_mgroups = '1111100000'
    return new_last_work_mgroups
    