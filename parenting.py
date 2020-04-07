def findMinKey(e): 
    return e[0]

def findMin(listToFind):
    listCopy = list(listToFind)
    listCopy.sort(key=findMinKey)
    return listCopy[0]

t = int(input())
for i in range(1, t + 1):
    entriesNum = int(input())
    activities = []
    for j in range(1, entriesNum + 1):
        activities.append(tuple(list(map(int, input().split(' ')))))
    remainingActivities = activities.copy()
    hopeless = False
    jNextAvail = 0
    cNextAvail = 0
    while(len(remainingActivities) > 0 and not hopeless):
        nextActivity = findMin(remainingActivities)
        if(nextActivity[0] >= jNextAvail):
            jNextAvail = nextActivity[1]
            remainingActivities.remove(nextActivity)
            targetIndex = activities.index(nextActivity)
            activities = activities[0:targetIndex] + list('J') + activities[targetIndex + 1:]
        elif(nextActivity[0] >= cNextAvail):
            cNextAvail = nextActivity[1]
            remainingActivities.remove(nextActivity)
            targetIndex = activities.index(nextActivity)
            activities = activities[0:targetIndex] + list('C') + activities[targetIndex + 1:]
        else:
            hopeless = True

    if(hopeless):
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
    else:
        print("Case #{}: {}".format(i, ''.join(activities)))
        
        