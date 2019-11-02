from api import select_muscle_groups
def workout(work_mgroups,diff,goal) :
    s = str(work_mgroups)
    arrA=list(s)
    newarrA=[1,1,1,1,1,1,1,1,1,1]

    #if work_mgroups is all 0s:
    #   work_mgroups = generate random mgroups (Caden)
    #   new_mgroups = inverse(Caden random shit)
    #else:
    #   work_mgroups = what we were passsed
    #   new_mgroups = all zeros
    #
    # new_mgroups is passed to database
    all_zeroes=0
    for i in range(len(arrA)):
        if (arrA[i]==1):
            all_zeros=1

    if all_zeroes==0:
        # all 0s
        arrA =list(str(select_muscle_groups()))
        for i in range(len(newarrA)):
            newarrA[i]=int(newarrA[i])-int(arrA[i])
    else:
        # work_mgroups stays the same
        arrA= list(str(work_mgroups))
        for i in range(len(newarrA)):
            newarrA[i]=0  
            

    # default settings
    modif = [1,1,1,1,1,1,1,1,1,1]
    mult = 1
    #

    thresh = [2,1,1,1,1,1,1,1,1,1]
    if goal=="massgain":
        modif = [.8,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]

    if goal=="weightloss":
        modif = [2,.6,.6,.6,.6,.6,.6,.6,.6,.6]

    if diff=="medium":
        mult=2

    if diff=="hard":
        mult=3

    if  diff=="extreme" :
        mult=5

    if  diff=="arnold" :
        mult=10
    a=0
    msg = "\nHere is your workout:\n"
    if  arrA[a]==1 :
        # Cardio
        n=random.choice([1,2,3])
        if  n==1 :
            msg+="Run: " + str(thresh[a]*mult*modif[a])+" miles\n"
        if  n==2 :
            msg+="Swim: " + str(.5*thresh[a]*mult*modif[a])+" miles\n"
        if  n==3 :
            msg+="Bike: " + str(2*thresh[a]*mult*modif[a])+" miles\n"

    a+=1

    if  arrA[a]==1 :
        # Back
        n=random.choice([1,2])
        if  n==1 :
            msg+="Chin-Ups: " + str(int(thresh[a]*mult*modif[a]*30))+" Reps\n"
        if  n==2 :
            msg+="Pull-Ups: " + str(int(thresh[a]*mult*modif[a]*30))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Core
        n=random.choice([1,2])
        if  n==1 :
            msg+="Sit-Ups: " + str(int(thresh[a]*mult*modif[a]*60))+" Reps\n"
        if  n==2 :
            msg+="Planking: " + str(int(thresh[a]*mult*modif[a]*15))+" Minutes\n"

    a+=1

    if  arrA[a]==1 :
        # Chest
        n=random.choice([1,2])
        if  n==1 :
            msg+="Push-Ups: " + str(int(thresh[a]*mult*modif[a]*60))+" Reps\n"
        if  n==2 :
            msg+="Bench Press: " + str(int(thresh[a]*mult*modif[a]*30))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Biceps
        msg+="Curls: " + str(int(thresh[a]*mult*modif[a]*45))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Triceps
        msg+="Dips: " + str(int(thresh[a]*mult*modif[a]*45))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Shoulders
        msg+="Front Raises: " + str(int(thresh[a]*mult*modif[a]*45))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Quads
        n=random.choice([1,2])
        if  n==1 :
            msg+="Leg Press: " + str(int(thresh[a]*mult*modif[a]*30))+" Reps\n"
        if  n==2 :
            msg+="Lunges: " + str(int(thresh[a]*mult*modif[a]*60))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Glutes
        n=random.choice([1,2])
        if  n==1 :
            msg+="Squat: " + str(int(thresh[a]*mult*modif[a]*30))+" Reps\n"
        if  n==2 :
            msg+="Deadlift: " + str(int(thresh[a]*mult*modif[a]*30))+" Reps\n"

    a+=1

    if  arrA[a]==1 :
        # Calves
        n=random.choice([1,2])
        if  n==1 :
            msg+="Standing Calf Raise: " + str(int(thresh[a]*mult*modif[a]*60))+" Reps\n"
        if  n==2 :
            msg+="Sitting Calf Raise: " + str(int(thresh[a]*mult*modif[a]*60))+" Reps\n"

    return msg,str(newarrA)
