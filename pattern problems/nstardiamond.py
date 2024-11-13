
#  Problem statement

# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.
# Example:

# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****
# *****
#  ***
#   *

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:

# 3

# Sample Output 1:

#   *
#  ***
# *****
# *****
#  ***
#   *    

for i in range(4):
    for j in range(3,i,-1):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")
    for j in range(3,i,-1):
        print(" ",end="")
    print("\n",end="")
    
for i in range(4):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,2*4-2*i-1):
        print("*",end="")
    for j in range(0,i):
        print(" ",end="")
    print("\n",end="")
