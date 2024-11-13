#  Problem statement

# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 

#   *
#  ***
# *****

# Detailed explanation ( Input/output format, Notes, Images ) 

for i in range(4):
    for j in reversed(range(4)):
        #print(i,j)
        if i>=j:
            print("*",end="")

        else:
            print(" ",end="")
            
    for j in range(0,i):
        print("*",end="")

    print("\n",end="")