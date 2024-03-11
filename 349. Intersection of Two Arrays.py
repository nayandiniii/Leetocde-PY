class Solution(object):
    def intersection(self, nums1, nums2):
        
        ans1 = set()
        for i in nums1:
            for j in nums2:
                if i ==j:
                    ans1.add(i)
        ans2 = list(ans1)
        return(ans2)
