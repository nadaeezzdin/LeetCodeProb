"""
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

def findMedianSortedArrays(arr1, arr2):
    result = []
    while (arr1 and arr2):

        if arr1[0] < arr2[0]:
            result.append(arr1[0])
            arr1.pop(0)
        else:
            result.append(arr2[0])
            arr2.pop(0)
    if arr1:
        result += arr1
    if arr2:
        result += arr2
    
    #return result

    index= len(result) // 2
    while result:
        if len(result) % 2 != 0:
            return  result[index] 
        else:
            return ((result[index] + result[index- 1])/ 2) 


print(findMedianSortedArrays([1,2],[3,4]))