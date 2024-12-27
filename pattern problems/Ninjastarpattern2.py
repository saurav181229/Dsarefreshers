def getNumberPattern(n: int) -> None:
    # Write your solution here.
    
    k = n-1
    mid = (2*n-1)/2
    for i in range(0,2*n):
        for j in range(0,2*n,1):
            #print(i,j)
            if i==0 or i==2*n-1:
                print(n,end="")
            elif j==0 or j==(2*n)-1:
                #print(j)
                print(n,end="")
            else:
                #print(i,j)
                
                print(" ",end="")
            
        print("\n",end="")
    
    pass

getNumberPattern(4)