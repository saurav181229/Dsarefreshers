
#  Rotated Triangle
# Easy
# 0/40
# Contributed by
# 100 upvotes
# Problem statement

# Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.
# Example:

# Input: ‘N’ = 3

# Output: 

# *
# **
# ***
# **
# *

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :

# 1  <= N <= 20
# Time Limit: 1 sec

# Sample Input 1:

# 3

# Sample Output 1:

# *
# **
# ***
# **
# *

# Sample Input 2 :

# 1

# Sample Output 2 :

# *


for  i in range(4):
    for j in range(0,i):
        print("*",end="");
    print("\n",end="")
    
for i in reversed(range(3)):
    for j in range(0,i):
        print("*",end="")
    print("\n",end="")