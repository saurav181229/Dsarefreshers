#  Problem statement

# Sam is making a Triangular painting for a maths project.

# An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers representing the row number.

# For every value of ‘N’, help sam to print the corresponding Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 
# 1
# 2 2 
# 3 3 3
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n",end="")
