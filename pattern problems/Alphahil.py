#  Problem statement

# Sam is curious about Alpha-Hills, so he decided to create Alpha-Hills of different sizes.

# An Alpha-hill is represented by a triangle, where alphabets are filled in palindromic order.

# For every value of ‘N’, help sam to return the corresponding Alpha-Hill.
# Example:

# Input: ‘N’ = 3

# Output: 
#     A
#   A B A
# A B C B A

# Detailed explanation ( Input/output format, Notes, Images ) 
# Import math library
import math
def alphaHill(n: int):
    # Write your solution from here.
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
    
        midpoint = i

        ch = ord('A')
        for j in range(0,2*i+1):
            print(chr(ch),end="")
            if j < midpoint:
                ch +=1
                
                

            else:
               
                ch-=1
                
                
        
        
         
  
        for j in range(i,n):
            print(" ",end="")
        print("\n",end="")
    pass

alphaHill(4)