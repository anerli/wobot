import random

MUSCLE_GROUPS = 10

def select_muscle_groups(usersettingarr):
    uslist = list(usersettingarr)
    uwlist = list("")
    inlist = list()
    invert = False

    #create a list with 10 '0's in it.
    for i in range(MUSCLE_GROUPS):
        uwlist.append('0')
        if uslist[i] != '1':
            inlist.append(i)
        else:
            invert = True
            break

    if invert:
        for i in uslist:
            i = 1 if i == 0 else 0
        return "".join(uslist)


    #pick a 5 muscle groups workout
    for i in range(5):
        if uslist.count('1') == MUSCLE_GROUPS:
            #TODO send '0000000000' to database
            break

        #grab muscle groups which haven't been done this cycle
        j = random.choice(inlist)

        uslist[j] = '1'
        uwlist[j] = '1'

    return "".join(uwlist)


def main():
    print(select_muscle_groups("0000011111"))

if __name__ == "__main__":
    # execute only if run as a script
    main()

