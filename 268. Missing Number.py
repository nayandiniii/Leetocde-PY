class Solution(object):
    def missingNumber(self, nums):
        #create a set with index range and subtract from the nums itself to get the number that doesn not exist in nums
        for s in set(range(len(nums) + 1)) - set(nums):
            return s
