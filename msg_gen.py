from api import select_muscle_groups
import random
def workout(work_mgroups,diff,goal) :
    s = str(work_mgroups)
    arrA=list(s)
    newarrA=[1,1,1,1,1,1,1,1,1,1]
    # for i in range(len(work_mgroups)):
    #     newarrA[i].append(1)
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
        if (int(arrA[i])==1):
            all_zeroes=1

    if all_zeroes==0:
        # all 0s
        arrA =list(str(select_muscle_groups()))
        for i in range(len(newarrA)):
            newarrA[i]=int(newarrA[i])-int(arrA[i])
    if all_zeroes==1:
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
        modif = [0.8,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6,1.6]

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
    msg = "\nArnold Says:\n"
    if  int(arrA[0])==1 :
        # Cardio
        n=random.choice([1,2,3])
        if  n==1 :
            
            if((thresh[0]*mult*modif[0])%1)!=0:
                if((thresh[0]*mult*modif[0])%1)<=.4:
                    cardio=int(thresh[0]*mult*modif[0])
                else:
                    cardio=int(thresh[0]*mult*modif[0])+1
            else:
                cardio=int(thresh[0]*mult*modif[0])
            if cardio==0:
                cardio=1
            msg+="Run: " + str(cardio)+" miles\n"
        
        if  n==2 :
            
            if((.5*thresh[0]*mult*modif[0])%1)!=0:
                if((.5*thresh[0]*mult*modif[0])%1)<=.4:
                    cardio=int(.5*thresh[0]*mult*modif[0])
                else:
                    cardio=int(.5*thresh[0]*mult*modif[0])+1
            else:
                cardio=int(thresh[0]*mult*modif[0]*.5)
            if cardio==0:
                cardio=1
            msg+="Swim: " + str(cardio)+" miles\n"
        
        if  n==3 :
            
            if((2*thresh[0]*mult*modif[0])%1)!=0:
                if((2*thresh[0]*mult*modif[0])%1)<=.4:
                    cardio=int(2*thresh[0]*mult*modif[0])
                else:
                    cardio=int(2*thresh[0]*mult*modif[0])+1
            else:
                cardio=int(thresh[0]*mult*modif[0]*2)
            if cardio==0:
                cardio=1
            msg+="Bike: " + str(cardio)+" miles\n"

    a+=1

    if  int(arrA[1])==1 :
        # Back
        n=random.choice([1,2])
        if  n==1 :
            msg+="Chin-Ups: 3 sets of " + str(int(thresh[1]*mult*modif[1]*5))+" Reps\n"
        if  n==2 :
            msg+="Pull-Ups: 3 sets of " + str(int(thresh[1]*mult*modif[1]*5))+" Reps\n"

    a+=1

    if  int(arrA[2])==1 :
        # Core
        n=random.choice([1,2])
        if  n==1 :
            msg+="Sit-Ups: 5 sets of " + str(int(thresh[2]*mult*modif[2]*10))+" Reps\n"
        if  n==2 :
            msg+="Planking: " + str(int(thresh[2]*mult*modif[2]*10))+" Minutes\n"

    a+=1

    if  int(arrA[3])==1 :
        # Chest
        n=random.choice([1,2])
        if  n==1 :
            msg+="Push-Ups: 5 sets of " + str(int(thresh[3]*mult*modif[3]*10))+" Reps\n"
        if  n==2 :
            msg+="Bench Press: 3 sets of " + str(int(thresh[3]*mult*modif[3]*5))+" Reps\n"

    a+=1

    if  int(arrA[4])==1 :
        # Biceps
        msg+="Curls: 3 sets of " + str(int(thresh[4]*mult*modif[4]*10))+" Reps\n"

    a+=1

    if  int(arrA[5])==1 :
        # Triceps
        msg+="Dips: 3 sets of " + str(int(thresh[5]*mult*modif[5]*5))+" Reps\n"

    a+=1

    if  int(arrA[6])==1 :
        # Shoulders
        msg+="Front Raises: 2 sets of " + str(int(thresh[6]*mult*modif[6]*10))+" Reps\n"

    a+=1

    if  int(arrA[7])==1 :
        # Quads
        n=random.choice([1,2])
        if  n==1 :
            msg+="Leg Press: 3 sets of " + str(int(thresh[7]*mult*modif[7]*5))+" Reps\n"
        if  n==2 :
            msg+="Lunges: 5 sets of " + str(int(thresh[7]*mult*modif[7]*10))+" Reps\n"

    a+=1

    if  int(arrA[8])==1 :
        # Glutes
        n=random.choice([1,2])
        if  n==1 :
            msg+="Squat: 3 sets of " + str(int(thresh[8]*mult*modif[8]*5))+" Reps\n"
        if  n==2 :
            msg+="Deadlift: 3 sets of " + str(int(thresh[8]*mult*modif[8]*5))+" Reps\n"

    a+=1

    if  int(arrA[9])==1 :
        # Calves
        n=random.choice([1,2])
        if  n==1 :
            msg+="Standing Calf Raise: 3 sets of " + str(int(thresh[9]*mult*modif[9]*15))+" Reps\n"
        if  n==2 :
<<<<<<< HEAD
            msg+="Sitting Calf Raise: " + str(int(thresh[9]*mult*modif[9]*45))+" Reps\n"

    # print(msg)
    s = ""
    for n in newarrA:
        s+=str(n)
=======
            msg+="Sitting Calf Raise: 3 sets of " + str(int(thresh[9]*mult*modif[9]*15))+" Reps\n"
    
    print(msg)
>>>>>>> master

    return msg, s

<<<<<<< HEAD
# if __name__ == "__main__":
#     workout('0000000000', ' ',' ')

=======
if __name__ == "__main__":
    workout('0000000000', ' ',' ')
>>>>>>> master
