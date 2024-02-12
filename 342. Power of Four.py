class Solution(object):
    def isPowerOfFour(self, n):

        for x in range(0,100): #keeping value of power in positive
            if n == pow(4,x): #check if the number is power of 4
                return True
            elif n ==1:  #default case
                return True
            if n<=0: # n must not be negative
                return False
