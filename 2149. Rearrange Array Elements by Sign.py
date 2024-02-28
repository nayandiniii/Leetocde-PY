class Solution(object):
    def rearrangeArray(self, nums):
        list1=[]
        list2=[]
        list3=[]

        for i in nums:
            if i>=0:
                list1.append(i)
            else:
                list2.append(i)
        j=0
        k=0
        while j< len(list1) and k < len(list2):
            list3.append(list1[j])
            list3.append(list2[k])
            j=j+1
            k=k+1
        return list3
