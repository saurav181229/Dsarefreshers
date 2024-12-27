
#  Problem statement

# Sam is researching on Alpha-Triangles. So, he needs to create them for different integers ‘N’.

# An Alpha-Triangle is represented by the triangular pattern of alphabets in reverse order.

# For every value of ‘N’, help sam to print the corresponding Alpha-Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 
# C
# C B 
# C B A

# Detailed explanation ( Input/out
def alphaTriangle(n: int):
    # Write your solution here.
    for i in range(n):
        ch = ord('C')

        for j in range(0,i+1):
            
            print(chr(ch),end="")
            ch-=1
        print("\n",end="")
    pass


alphaTriangle(3)