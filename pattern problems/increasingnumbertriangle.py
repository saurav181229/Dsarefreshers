
# print 
# 1
# 23
# 456
def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    k = 1
    for i in range(n+1):
       
        for j in range(1,i+1):
            print(k,end="")
            k+=1
        print("\n",end="")
            
        
    pass
nNumberTriangle(3)