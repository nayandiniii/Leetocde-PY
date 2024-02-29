class Solution(object):
    def integerBreak(self, n):
        
        if (n==2 or n==3):
            return (n-1)
        
        res = 1
        while n>4:
            n = n-3
            res = res*3
        return (n*res)
        
