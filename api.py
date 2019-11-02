import random

MUSCLE_GROUPS = 10

def select_muscle_groups():
    uwlist = list("")
    indexList = list()

    #create a list with 10 '0's in it.
    for i in range(MUSCLE_GROUPS):
        uwlist.append('0')
        indexList.append(i)

    #pick a 5 muscle groups workout
    for i in range(5):
        #grab muscle groups which haven't been done this cycle
        j = random.choice(indexList)

        del indexList[indexList.index(j)]
        uwlist[j] = '1'

    return "".join(uwlist)

if __name__ == "__main__":
    print(select_muscle_groups())