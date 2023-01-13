def findRepeatedNumber(array: list,sizeArray: int ) -> tuple:
    i = 0
    found = False
    while(not found and (i <sizeArray)):
        found = isIn(array[:i]+array[i+1:], sizeArray-1, array[i])
        if(found):
            return (i,array[i])
        i+=1
    return (-1,None)

def isIn(array: list, sizeArray: int, elem: int)-> bool:
    for i in range(sizeArray):
        if(array[i] == elem):
            return True
    return False

array = [2,1,4,3,3]
answer = findRepeatedNumber(array, len(array))
print("Repeated number is at  index: {0} and is number: {1}".format(answer[0],answer[1]))