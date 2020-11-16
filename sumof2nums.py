
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