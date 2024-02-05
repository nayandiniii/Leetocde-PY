class Solution(object):
    def largestGoodInteger(self, num):
        n = 3
        list1 = []

        # Find sequences of 3 consecutive equal digits
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                strings = num[i] + num[i+1] + num[i+2]
                list1.append(strings) #if we convert to int here then i won't display "000"

        # Sort the list in descending order
        list1.sort(reverse=True)

        # Return the largest element in the sorted list
        if list1:
            return list1[0]
        else:
            return ""

