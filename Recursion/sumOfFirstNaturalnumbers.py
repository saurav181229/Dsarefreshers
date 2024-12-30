# Sum of first N Natural Numbers


# 107

# 4
# Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

# Examples:

# Example 1:
# Input: N=5
# Output: 15
# Explanation: 1+2+3+4+5=15

# Example 2:
# Input: N=6
# Output: 21
# Explanation: 1+2+3+4+5+6=15

def sumOnNumbers(n,sum):
    if n<1:
        return sum+n
    return sumOnNumbers(n-1,sum+n)



#using funtional method

def sumUsingfuntionalMethod(n):
    if n ==0:
        return 0 
    return n+sumUsingfuntionalMethod(n-1)

a = sumUsingfuntionalMethod(3)
print(a)