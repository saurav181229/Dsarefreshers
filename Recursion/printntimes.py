def printNTimes(i,n):
    if(i>n): return
    print(i)
    printNTimes(i+1,n)

#printNTimes(0,5)

def PrintNtimeBackTracking(i,n):
    if i<1:
        return
    PrintNtimeBackTracking(i-1,n)
    print(i)

#PrintNtimeBackTracking(3,3)
def PrintNTimesReverse(i,n):
    if i>n: return 
    PrintNTimesReverse(i+1,n)
    print(i)


PrintNTimesReverse(1,3)