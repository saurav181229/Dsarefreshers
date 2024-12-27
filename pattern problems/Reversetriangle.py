
#  Problem statement

# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 

# *****
#  ***
#   *

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 20
# Time Limit: 1 sec

def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(n):
        
        for j in range(i):
            print(" ",end="")
    
        for j in range(2*n-2*i-1):
            print("*",end="")
        
        for j in range(i):
            print(" ",end="")        

        print("\n",end="")

nStarTriangle(3)