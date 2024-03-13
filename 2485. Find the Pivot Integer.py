class Solution(object):
    def pivotInteger(self, n):
        count1=0
        count2=0
        for i in range(1,n+1):
            l = list(range(1,i+1))
            r = list(range(i,n+1))
            if sum(l) == sum(r):
                return i
        return -1 
