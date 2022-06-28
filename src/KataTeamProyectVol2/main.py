from array import array
import re 
def CreateRange(x):
    y =[i for i in re.split('(-?\d+\.?\d*)',x) if i !='']
    print(y)
    range = [int(m) for m in y if m.isdigit()]
    if y[0] == '(':
        v1 = range[0] + 1 
    else:
        v1 = range[0]
    if y[-1] == ']':
        v2 = range[1] + 1
    else:
        v2 = range[1]
    output=[v1,v2]
    return output 



def integer_range_contains(defaultrange, inputrange):
    defaultrange = [i for i in range(defaultrange[0], defaultrange[1])]
    for i in defaultrange:
        if defaultrange[i] in inputrange:
            return True
        else:
            return False
    

def getAllPoint(inputrange):
    return [i for i in range(inputrange[0], inputrange[1])]

def ContainsRange(arr1, arr2):
    arr1 = [i for i in range(arr1[0], arr1[1])]
    arr2 = [j for j in range(arr2[0], arr2[1])]
    if max(arr2) > max(arr1) or min(arr2)<min(arr1):
        return False
    else :
        return True
    

def endPoints(range):
    
    return val

def Equals(range1, range2):
    if range1 == range2:
        return True
    else:
        return False

def overlapsRange():
    return