class Solution(object):
    def missingNumber(self, nums):
        
        for s in set(range(len(nums) + 1)) - set(nums):
            return s
