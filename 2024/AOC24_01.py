#Main Variables
difference = 0
similarity = 0
leftList = []
rightList = []
rightCount = {}

#Read Input File
file = open("resources/AOC24_01.txt", "r")

#Place in Arrays
for line in file:
    content = line.split()
    if(len(content) == 2):

        leftList.append(int(content[0]))
        rightList.append( int(content[1]) )

        if rightCount.__contains__(int(content[1])):
            rightCount[int(content[1])] += 1
        else:
            rightCount[int(content[1])] = 1

#Order
leftList.sort()
rightList.sort()

#Calculate Difference and Similarity
for i in range(0,len(leftList)):
    difference += abs(leftList[i]-rightList[i])

    if(rightCount.__contains__(leftList[i])):
        similarity += leftList[i] * rightCount[leftList[i]]

#Return Answers
print("The difference number is: ", difference)
print("The similarity number is: ", similarity)