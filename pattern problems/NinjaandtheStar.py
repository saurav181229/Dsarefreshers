#  Problem statement

# Ninja has been given a task to print the required star pattern and he asked your help for the same.

# You must return an ‘N’*’N’ matrix corresponding to the given star pattern.
# Example:

# Input: ‘N’ = 4

# Output: 

# ****
# *  *
# *  *
# ****

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 10^2
# Time Limit: 1 sec

# Sample Input 1:

# 3

# Sample Output 1:

# ***
# * *
# ***

# Sample Input 2 :

# 5

# Sample Output 2 :

# *****
# *   *
# *   *
# *   *
# *****

# Sample Input 3 :

# 8

# Sample Output 3 :

# ********
# *      *
# *      *
# *      *
# *      *
# *      *
# *      *
# ********

def getStarPattern(n: int) -> None:
    # Write your solution here.
    for i in range(n):
        for j in range(n):
            if i ==0 or i==n-1:
                print("*",end="")
            elif j==0 or j==n-1:
                # print("helo",j,i,end="")
                print("*",end="")
            else:
                print(" ",end="")
        print("\n",end="")
    pass

getStarPattern(4)