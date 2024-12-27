#  Problem statement

# Sam is making a forest visualizer. An N-dimensional forest is represented by the pattern of size NxN filled with ‘*’.

# An N/2-dimensional forest is represented by the lower triangle of the pattern filled with ‘*’.

# For every value of ‘N’, help sam to print the corresponding N/2-dimensional forest.
# Example:

# Input:  ‘N’ = 3

# Output: 
# * 
# * *
# * * *

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n", end="")
