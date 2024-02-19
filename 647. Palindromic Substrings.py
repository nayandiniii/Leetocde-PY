class Solution(object):
    def countSubstrings(self, s):
        count=0

        for c in range(2*len(s)-1): #to calculate spaces also if more than on word
            left= c//2 #calculates the index of left pointer
            right = left + c%2 #to calculate the space

            while left>=0 and right<len(s) and s[left]==s[right]:
                count +=1
                left-=1
                right+=1
        return count
        
