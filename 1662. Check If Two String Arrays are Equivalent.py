class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        
        list1 = []
        i=0
        j=0
        ans1=" " #to store the concatenated string of word1 
        ans2= " "  # to store the concatednated string of word2
        for i in range(len(word1)):
            ans1=  ans1 + word1[i] #join the items to form a string
            i=i+1
        for j in range(len(word2)):
            ans2 = ans2 + word2[j]
            j=j+1
        print(ans1)
        if ans1 == ans2: #comparing the two string values
            return True
        else :
            return False
        
