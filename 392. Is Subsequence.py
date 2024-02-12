class Solution(object):
    def isSubsequence(self, s, t):
        #initilaizing index variables 
        i=0
        j=0

        #we iterate through each alphabet and kepe on checking if they are same
        #if they don't match we move to the end of main string to check it
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1 # increase value of i in subsbtring 
            j+=1 #if i matches j when we iterate through the length then it is
            # subsequence
        return True if i==len(s) else False
        
