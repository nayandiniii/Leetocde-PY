
class Solution(object):
    def numIdenticalPairs(self, nums):
        
        count =0
        
        for i in range(len(nums)): #iterates through 0 to len(nums)-1
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count=count+1
        return count
        
```
