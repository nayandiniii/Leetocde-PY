#Baraa
class Solution:
    def closeStrings(self, word1, word2) :
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        if set(word1) != set(word2) or len(word1) != len(word2):
            return False
        #If both strings have same letters and same number of frequencies 
        #eg: aaab , bbba  both have (a,b) and both have 3 frequencies of certain letter and 1 frequency of another letter
        if c1 == c2 or collections.Counter(c1.values()) == collections.Counter(c2.values()):
            return True
        
        
        
        
        
        
