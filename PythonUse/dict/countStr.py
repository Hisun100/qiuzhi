def findFirstRepeat(A, n):
    strDict = {} #创建空字典
    for s in A:
        if not s in strDict:
            strDict[s] = 1
        else:
            strDict[s] +=1
    return strDict
        
print(findFirstRepeat("qywyer23tdd",11))


def findFirstRepeat(A, n):
    strDict = {} #创建空字典
    for s in A:
        if not s in strDict:
            strDict[s]=1
        else:
            return s
        
print(findFirstRepeat("qywyer23tdd",11))
            
            
