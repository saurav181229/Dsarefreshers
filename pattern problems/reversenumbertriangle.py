#  Problem statement

# Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the Reverse N-Number Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 

# 1 2 3
# 1 2
# 1

for i in reversed(range(5)):
    for j in range(1,i):
        print(j,end=" ")
    print("\n",end="")
