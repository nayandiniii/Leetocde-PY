class Solution(object):
    def numberOfMatches(self, n):
        result=0
        while n != 1 :
            if n%2==0:
                result = result + n/2
                n = n/2
            else:
                result = result + (n-1)/2
                n= ((n-1)/2)+1
        return result
                
