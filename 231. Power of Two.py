class Solution(object):
    def isPowerOfTwo(self, n):
        
        for i in range(0,100):
            if n ==pow(2,i):
                return True
        return False
        
