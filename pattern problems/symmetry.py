
#  Problem statement

# Sam is curious about symmetric patterns, so he decided to create one.

# For every value of ‘N’, return the symmetry as shown in the example.
# Example:

# Input: ‘N’ = 3

# Output: 
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 25
# Time Limit: 1 sec

# Sample Input 1:

# 3

# Sample Output 1:

# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *

def symmetry(n: int):
    # Write your solution here.
    spaces = 2*n-2 
    for i in range(1,2*n-1+1):
        stars = i
        if i>n: stars = 2*n-i;
        
        for j in range(0,stars):
            print("*",end="")
        for j in range(0,spaces):
            print(" ",end="")
        for j in range(0,stars):
            print("*",end="")
        
        if i+1 >n:
                spaces+=2 
            #print(spaces)
        else:
            spaces-=2   
             
        print("\n",end="")
    pass

symmetry(3)
