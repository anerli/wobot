num_mgroups = 10
import random

def select_muscle_groups():
    s = ""
    zerocount = 5
    onecount = 5

    random.seed()
    
    while(True):
        
        if zerocount == 0 & onecount == 0:
            break
        if(random.choice([True, False]) and zerocount > 0):
            s += "0"
            zerocount -= 1
        elif(onecount > 0):
            s += "1"
            onecount -= 1
        #print(zerocount)
        #print(onecount)
        #print(s)
    return s

if __name__=="__main__":
    print(select_muscle_groups())