
def listcompare(expectedList ,actualList):

    try:

        if len(expectedList) == len(actualList):
            i = 0
            for i in range(0,len(actualList)):
                if expectedList[i] == actualList[i]:
                    i = i+ 1
                    if i == len(actualList):
                        print("Matched")
                        return True
                else:
                    print("List Does not match")
                    return False
                    break
        else:
            print("List Length does not match")
            return False
    except :
        print("List Len does not match")
        return False



A = [1,2,3,3]
B = [1,2,3,3]


atique = listcompare(expectedList=A,actualList=B)
print(atique)