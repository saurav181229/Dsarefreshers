# actorial of a Number : Iterative and Recursive


# 107

# 4
# Problem Statement: Given a number X,  print its factorial.

# To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

# Note: X  is always a positive number. 

# Examples:

# Example 1:
# Input: X = 5
# Output: 120
# Explanation: 5! = 5*4*3*2*1

# Example 2:
# Input: X = 3
# Output: 6
# Explanation: 3!=3*2*1
# Solution
# Disclaimer: Don't jump directly to the solution, try it out yourself first.

# Solution 1: Iterative

# Approach:

# Since the factorial of X  will be the product of the number itself and all its preceding numbers we can run loop i, from 1 to X. In every iteration current i, is multiplied with the product so far.  

def factorialofN(n):
    if n==0:
        return 1
    return n* factorialofN(n-1)

a = factorialofN(4)
print(a)