#Main Variables
items = []
total = 0

#Read Input File
file = open("2024/resources/AOC24_02.txt", "r")

def CheckDifference(num1, num2):
    if abs(num1-num2) == 0 or abs(num1-num2) > 3:
        return False
    return True

def CheckDirection(num1, num2, mode):
    
    if mode == 1 and int(num2) <= num1:
        return False
    elif mode == 0 and int(num2) >= num1:
        return False
    return True

def RunChecks(item):

    problem = 0
    previous = -1
    mode = -1

    for i in range(len(item)):
        current = int(item[i])

        if previous == -1:
            previous = current
        else:

            if i == 1:
                if current > previous:
                    mode = 1
                elif current < previous:
                    mode = 0
            else:

                #Check Direction
                if(not CheckDirection(previous, current, mode)):
                    problem = current

            #Check Difference
            if not CheckDifference(previous, current):
                problem = current

            previous = current

    
    return problem

#Place in Arrays
for line in file:
    
    content = line.split()

    items.append(content)

#Run Rules
for item in items:

    changed = False
    newItem = []

    problem = RunChecks(item)
    if problem == 0:
        total += 1
    else:


        for x in range(0, len(item)):
            new = []

            for i in range(0,len(item)):
                if(i != x):
                    new.append(item[i])

            problem = RunChecks(new)

            if problem == 0:
                total += 1
                changed = True
                newItem = new
                break


    #Print Changed
    if changed:
        print(newItem,"->",item, problem == 0)
    else:
        print(item, problem == 0)


#Print Final total
print(total)