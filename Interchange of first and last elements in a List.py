def swapList(newList):
    size=len(newList)
    temp=newList[0]
    newList[0]=newList[size-1]
    newList[size-1]=temp
    return newList
List=[2,4,6,8]
print(swapList(List))
