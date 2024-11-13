#  Problem statement

# Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.

# You are required to print the pattern as shown in the examples below.
# Example:

# Input: ‘N’ = 3

# Output: 

# 1
# 0 1
# 1 0 1



k=0
for i in range(4):
    if i%2==1:
        k = 1
    for j in range(0,i):
        k = int(not(k))
        print(k,end="")
    print("\n",end="")