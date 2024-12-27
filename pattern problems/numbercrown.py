#  Problem statement

# Aryan and his friends are very fond of the pattern. They want to make the Reverse N-Number Crown for a given integer' N'.

# Given 'N', print the corresponding pattern.
# Example:

# Input: ‘N’ = 3

# Output: 

# 1         1
# 1 2     2 1
# 1 2 3 3 2 1

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 20
# Time Limit: 1 sec
def numberCrown(n: int) -> None:
    # Write your solution here.
    k=n
    for i in range(n):
        for j in range(0,i+1):
            p=j+1
            print(j+1,end="")
        for j in range(0,2*k-2):
            print(" ",end="")
       
        k-=1
        for j in range(p,0,-1):
        # print("3rd loop",j)
            print(j,end="")

        print("\n",end="")
    pass

numberCrown(3)