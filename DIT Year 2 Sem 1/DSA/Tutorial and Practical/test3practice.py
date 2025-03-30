

def createList(numList, i):
    if i == len(numList)-1:
        return numList
    else:
        if numList[i] > numList[i+1]:
            numList[i+1] = numList[i]
            return createList(numList, i+1)
        else:
            return createList(numList, i+1)


print(createList([1,2,1],0))