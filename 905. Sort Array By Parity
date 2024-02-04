class Solution(object):
    def sortArrayByParity(self, nums):
        # lists to store even and odd numbers 
        final1=[]
        final2=[]
        for i in nums:
            if i%2==0: #append even numbers
                final1.append(i)
        for j in nums:
            if j%2!=0: #append odd numbers 
                final1.append(j)
        result=final1+final2 #joining two lists ( order in the final result can be in any sequence for first : even then : odd)
        return result
        
