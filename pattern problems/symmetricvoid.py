#  Problem statement

# Sam is curious about symmetric patterns, so he decided to create one.

# For every value of ‘N’, return the symmetry as shown in the example.
# Example:

# Input: ‘N’ = 3

# Output: 
# * * * * * * 
# * *     * * 
# *         * 
# *         * 
# * *     * * 
# * * * * * * 

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 25
# Time Limit: 1 sec

def symmetry(n: int):
    # Write your solution from here.
    inis = 0
    for i in range(n):
       
        for j in range(0,n-i):
            print("*",end="")
        
        for j in range(0,inis):
            print(" ",end="")
        for j in range(0,n-i):
            print("*",end="")
        
        inis+=2;
        print("\n",end="")
    inis-=2
    #print(inis)
    for i in range(n):
           
        for j in range(0,i+1):
            print("*",end="")
        
        for j in range(0,inis):
            print(" ",end="")
        for j in range(0,i+1):
            print("*",end="")
        
        inis-=2;
        print("\n",end="")
    pass

symmetry(3)