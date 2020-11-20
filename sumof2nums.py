"""
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
'''
def twoSum( nums, target):
    count=0
    for i in range(len(nums)):
        for j in range( i+1, len(nums)):
            if nums[i] + nums[j] == target :
                count +=1
                break
        if count == 1:
            return [i,j]
            break

print(twoSum([3,2,4],6))

'''

       


def twoSum2( nums, target):

    sub=[]
    result=[]
    for i in nums:
        sub.append(target-i)
    for i in range(len(sub)):
        if sub[i] in nums  :
            if i!= nums.index(sub[i]):
                result.append([i,nums.index(sub[i])])            
    return result[0]

print(twoSum2([3,2,4],6))
print(twoSum2([2,7,11,15],9))