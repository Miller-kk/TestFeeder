import random

def arithOpGen(ropIndex):
    arithOpList = ["*=", "+=", "%=", "/="]
    
    if(ropIndex <= 2):
        aopIndex = random.randint(0,1)
        return arithOpList[aopIndex]  
    else:
        aopIndex = random.randint(2,3)
        return arithOpList[aopIndex]


def relOpGen():
    relOpList = ["==", ">", ">=", "<", "<="]
    ropIndex = random.randint(0, 4)
    return (ropIndex,relOpList[ropIndex])