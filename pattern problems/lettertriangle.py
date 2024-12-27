#  Problem statement

# Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Letter Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 

# A
# A B
# A B C

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 20
# Time Limit: 1 sec

def nLetterTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n):
        for j in range(0,i+1):
            print(chr(65 + j),end=" ")
        print("\n",end="")
    pass
nLetterTriangle(5)
