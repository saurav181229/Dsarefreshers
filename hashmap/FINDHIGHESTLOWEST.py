# ind the highest/lowest frequency element
# 131
# 18

# Problem Statement: Given an array of size N. Find the highest and lowest frequency element.

# Pre-requisite: Hashing Theory and  Counting frequencies of array elements

# Examples:

# Example 1:
# Input: array[] = {10,5,10,15,10,5};
# Output: 10 15
# Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

# Example 2:


# Input: array[] = {2,2,3,4,4,2};
# Output: 2 3
# Explanation: The frequency of 2 is 3, i.e. the highest and the frequency of 3 is 1 i.e. the lowest.


def MinAndMaxFrequency(arr):
    freq = {}

    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i],0)+1

    #find max value
    min = 999
    max = 0
    min_Key=0
    max_Key=0
    for key in freq:
        if freq[key]>max:
            max_Key = key
            max = freq[key]
    for key in freq:
        if freq[key]<min:
            min_Key = key
            min = freq[key]

    print("max frqquency",max_Key,max)
    print("max frqquency",min_Key,min)

MinAndMaxFrequency([2,2,3,4,4,2])