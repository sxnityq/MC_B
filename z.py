def canJump(nums) -> bool:

    maxReachableIndex = 0
    stepsCollector = [0] * len(nums)
    
    print(nums)
    
    if len(nums) == 1:
        return 0
    if nums[0] >= len(nums):
        return 1
    
    for index, step in enumerate(nums, 0):
        if step + index >= len(nums) - 1:
            return stepsCollector[index] + 1
        
        if step + index > maxReachableIndex:
            collectorIndexValueToAdd = stepsCollector[index]
            for j in range(maxReachableIndex, step + index + 1):
                if stepsCollector[j] == 0: 
                    stepsCollector[j] += collectorIndexValueToAdd + 1
            maxReachableIndex = step + index
    return False
        
            
#print(canJump([1,2,3]))
#print(canJump([2,3,0,1,4]))
#print(canJump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
print(canJump([3,2,1,0,4]))
#print(canJump([5,2,1,2,5,2,6,8,1,9,3,5,8,0,2]))

#print(canJump([5,4,0,1,3,6,8,0,9,4,9,1,8,7,4,8]))
