class Solution(object):
    def firstUniqChar(self, s):
        char_count = {}
        
        # Count occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Find the index of the first unique character
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        
        # If no unique character found, return -1
        return -1
