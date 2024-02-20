class Solution:
    def findErrorNums(self, nums):
        x, y = 0, 0 #error numbers to be corrected and displayed
        tmp = 0 #to calculate the actual sum of numbers
        n = len(nums)
        expected_sum = n * (n + 1) // 2 #sum of sequence of numbers
        s = set() #to avoid duplicates in the final list

        for i in nums:
            if i in s:
                y = i #if it is in set that means i is duplicate value
            else:
                s.add(i) #if not in set then add it to the set
                tmp += i #add the values in the set (the duplicate is excluded)

        x = expected_sum - tmp #total sum of numbers - sum of numbers without duplicate
        return [y, x]
