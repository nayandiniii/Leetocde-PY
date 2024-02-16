class Solution(object):
    def firstPalindrome(self, words):
        l1=[]
        for i in words:
            if i==i[::-1]:
                return i
        return ""
