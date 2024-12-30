# everse a given Array


# 231

# 9
# Problem Statement: You are given an array. The task is to reverse the array and print it. 

# Examples:

# Example 1:
# Input: N = 5, arr[] = {5,4,3,2,1}
# Output: {1,2,3,4,5}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

# Example 2:
# Input: N=6 arr[] = {10,20,30,40}
# Output: {40,30,20,10}
# Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

def reverseArray(arr):
    n = len(arr)
    a = 0
    b=n-1
    temp = 0
    while a <=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b]=temp
        a = a+1
        b-=1
    print(arr)

#reverseArray([1,2,3,4])
        
def swapUsingrecurssion(l,r,arr):
    if l>=r:
        #ßprint(arr)
        return arr
    arr[l],arr[r] = arr[r],arr[l]

    return swapUsingrecurssion(l+1,r-1,arr)
     
a = swapUsingrecurssion(0,4,[1,2,3,4,5])
print(a)