#  Problem statement

# Sam is planting trees on the upper half region (separated by the left diagonal) of the square shared field.

# For every value of ‘N’, print the field if the trees are represented by ‘*’.
# Example:

# Input: ‘N’ = 3

# Output: 
# * * *
# * *
# *

for i in reversed(range(5)):
    for j in range(i):
        print("*",end=" ")
    print("\n",end="")